#!/usr/bin/env python3
"""
Compute a dense-vector index over the RAG chunks (optional layer).

Reads `exports/rag/chunks.jsonl`, embeds each chunk's `context_header + text`
(the header is the deterministic contextual prefix built by build_rag.py — this
is "contextual retrieval": the embedded string is self-describing, not a naked
mid-section paragraph), and writes:

  * exports/rag/embeddings.npz        float32 L2-normalised vectors + chunk_ids
  * exports/rag/embeddings.meta.json  provider, model, dim, count, source hash

These artefacts are **git-ignored on purpose**: they are large, binary, and
model-version-dependent, so they must not enter the deterministic CI staleness
gate the way the text exports do. Rebuild them on demand.

Usage:
  python scripts/build_embeddings.py                 # auto provider
  python scripts/build_embeddings.py --provider openai
  python scripts/build_embeddings.py --provider hash # offline plumbing/CI
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import embeddings as emb  # noqa: E402

RAG = Path("exports/rag")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--provider", default="auto",
                    help=f"auto | {' | '.join(emb.available())}")
    ap.add_argument("--model", default=None, help="override the provider's default model")
    args = ap.parse_args()

    chunks_path = RAG / "chunks.jsonl"
    if not chunks_path.exists():
        print("No chunks.jsonl — run: python scripts/build_rag.py", file=sys.stderr)
        return 2
    rows = [json.loads(l) for l in chunks_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    ids = [r["chunk_id"] for r in rows]
    texts = [f"{r.get('context_header','')}\n{r['text']}" for r in rows]

    provider = emb.get_provider(args.provider, args.model)
    print(f"Embedding {len(texts)} chunks with {provider.key} (dim {provider.dim})…",
          file=sys.stderr)
    vecs = provider.embed(texts)
    assert vecs.shape == (len(texts), provider.dim), vecs.shape

    RAG.mkdir(parents=True, exist_ok=True)
    np.savez(RAG / "embeddings.npz",
             vectors=vecs.astype(np.float32),
             chunk_ids=np.asarray(ids, dtype=object))
    src_hash = hashlib.sha256(chunks_path.read_bytes()).hexdigest()[:16]
    (RAG / "embeddings.meta.json").write_text(json.dumps({
        "provider": provider.name,
        "model": provider.model,
        "key": provider.key,
        "dim": provider.dim,
        "count": len(ids),
        "chunks_sha256_16": src_hash,
        "note": "Query embeddings must use the same provider+model (see 'key'). "
                "Git-ignored: non-deterministic across providers/model versions. "
                "Rebuild with scripts/build_embeddings.py.",
    }, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote embeddings.npz ({len(ids)} × {provider.dim}, {provider.key}) "
          f"and embeddings.meta.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
