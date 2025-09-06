# Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2025-09-06 | Introduce Qdrant alongside existing Weaviate support | Provide optional open-source vector store alternative; reduce vendor lock-in; enable benchmarking & fallback. |
| 2025-09-06 | Use env var `VECTOR_DB_TYPE` for backend selection | Simple, explicit runtime selection mechanism without code changes per deploy. |
| 2025-09-06 | Implement healthcheck using Qdrant `/readyz` endpoint | `/health` not available; root path JSON caused compose to remain in `starting`; `/readyz` returns deterministic readiness text. |
| 2025-09-06 | Implement `VectorDB` abstraction with `QdrantVectorDB` | Enables pluggable backends and keeps optional deps isolated; simplifies tool and service integration. |
| 2025-09-06 | Add `QdrantSearch` tool gated by `VECTOR_DB_TYPE` | Provides immediate utility for Qdrant search workflows; minimal inputs; safe failure modes. |
| 2025-09-06 | Enforce explicit submodule imports in docs/CI | Avoid heavy top-level imports; reduce optional dependency pressure at import time. |
