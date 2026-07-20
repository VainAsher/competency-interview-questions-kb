#!/usr/bin/env python3
"""
Pluggable embedding providers for the RAG layer.

Dense embeddings are an *optional* enhancement — the core pipeline
(build_rag.py, and rag_query.py's BM25 path) has zero dependencies beyond
PyYAML and always works. This module is only imported when someone asks for
dense or hybrid retrieval, and it degrades gracefully:

  provider precedence (auto):  openai  ->  local  ->  hash

  * openai  — text-embedding-3-small (1536-d). Needs `pip install openai` and
              OPENAI_API_KEY. Real semantics, cheap, no local model.
  * local   — sentence-transformers all-MiniLM-L6-v2 (384-d). Needs
              `pip install sentence-transformers`. Fully offline once cached.
  * hash    — a deterministic hashing bag-of-words embedder (256-d), pure
              Python + numpy. **No real semantics** — it exists so the fusion
              plumbing is testable offline and in CI without heavy deps or a
              network. Never use it for real retrieval quality.

Every provider returns L2-normalised float32 vectors, so cosine similarity is a
plain dot product. Query and corpus MUST use the same provider+model; the model
identity is recorded in the embeddings sidecar and checked at query time.
"""
from __future__ import annotations

import hashlib
import os
import re
from dataclasses import dataclass

import numpy as np

TOKEN_RE = re.compile(r"[a-z0-9]+")


def _l2(v: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(v, axis=-1, keepdims=True)
    return v / np.where(n == 0, 1, n)


@dataclass
class Provider:
    name: str
    model: str
    dim: int

    def embed(self, texts: list[str]) -> np.ndarray:  # pragma: no cover
        raise NotImplementedError

    @property
    def key(self) -> str:
        return f"{self.name}:{self.model}"


class OpenAIProvider(Provider):
    def __init__(self, model: str = "text-embedding-3-small"):
        from openai import OpenAI  # lazy
        self._client = OpenAI()
        dim = {"text-embedding-3-small": 1536, "text-embedding-3-large": 3072}.get(model, 1536)
        super().__init__("openai", model, dim)

    def embed(self, texts: list[str]) -> np.ndarray:
        out: list[list[float]] = []
        for i in range(0, len(texts), 256):          # API batch limit headroom
            batch = [t.replace("\n", " ")[:8000] for t in texts[i:i + 256]]
            resp = self._client.embeddings.create(model=self.model, input=batch)
            out.extend(d.embedding for d in resp.data)
        return _l2(np.asarray(out, dtype=np.float32))


class LocalProvider(Provider):
    def __init__(self, model: str = "sentence-transformers/all-MiniLM-L6-v2"):
        from sentence_transformers import SentenceTransformer  # lazy
        self._m = SentenceTransformer(model)
        super().__init__("local", model, self._m.get_sentence_embedding_dimension())

    def embed(self, texts: list[str]) -> np.ndarray:
        v = self._m.encode(texts, convert_to_numpy=True, normalize_embeddings=True,
                            show_progress_bar=False)
        return v.astype(np.float32)


class HashProvider(Provider):
    """Deterministic, dependency-free, and semantically meaningless.
    Hashes tokens into a fixed-width vector — for plumbing/CI only."""
    def __init__(self, dim: int = 256):
        super().__init__("hash", f"hash-{dim}", dim)

    def embed(self, texts: list[str]) -> np.ndarray:
        out = np.zeros((len(texts), self.dim), dtype=np.float32)
        for i, t in enumerate(texts):
            for tok in TOKEN_RE.findall(t.lower()):
                h = int.from_bytes(hashlib.blake2b(tok.encode(), digest_size=8).digest(), "big")
                out[i, h % self.dim] += 1.0
        return _l2(out)


def available() -> list[str]:
    have = []
    try:
        import openai  # noqa: F401
        if os.environ.get("OPENAI_API_KEY"):
            have.append("openai")
    except ImportError:
        pass
    try:
        import sentence_transformers  # noqa: F401
        have.append("local")
    except ImportError:
        pass
    have.append("hash")
    return have


def get_provider(name: str = "auto", model: str | None = None) -> Provider:
    if name == "auto":
        name = available()[0]
    if name == "openai":
        return OpenAIProvider(model or "text-embedding-3-small")
    if name == "local":
        return LocalProvider(model or "sentence-transformers/all-MiniLM-L6-v2")
    if name == "hash":
        return HashProvider(int(model) if model else 256)
    raise ValueError(f"unknown provider '{name}'; available: {available()}")


def provider_from_meta(meta: dict) -> Provider:
    """Rebuild the exact provider an index was written with, for query-time
    embedding. The corpus and the query MUST share provider+model."""
    name = meta["provider"]
    if name == "hash":
        return HashProvider(int(meta["dim"]))
    if name == "openai":
        return OpenAIProvider(meta["model"])
    if name == "local":
        return LocalProvider(meta["model"])
    raise ValueError(f"unknown provider in meta: {name}")
