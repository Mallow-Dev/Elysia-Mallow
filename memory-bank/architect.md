# MemoriPilot: System Architect

## Overview

This document records current and planned architectural structure. Current focus: pluggable vector store backends (Weaviate, Qdrant).

## Vector Store Abstraction (Implemented)

### Goals

- Allow runtime selection of vector backend via environment (`VECTOR_DB_TYPE`).
- Minimise conditional logic spread—centralise in a provider/factory.
- Provide consistent interface for: create_collection, upsert_vectors, query, delete, aggregate (if supported).

### Implemented Interface (Python)

```python
class VectorDB(ABC):
    def connect(self, **kwargs) -> None: ...
    def create_collection(self, name: str, vector_size: int) -> None: ...
    def insert_vectors(self, collection: str, vectors, payloads) -> None: ...
    def search_vectors(self, collection: str, query_vector, limit: int = 10) -> list[dict]: ...
```

### Factory

```python
from elysia.api.vector_db import create_vector_db, get_vector_db_from_env

db = create_vector_db("qdrant", url=os.getenv("QDRANT_URL"))
# or
db = get_vector_db_from_env()
```

### Qdrant Notes

- Readiness endpoint: `/readyz` (text: "all shards are ready").
- Distinct concepts: Collections, points (id, vector, payload).
- Supports filtering with structured conditions; initial version may defer advanced filter translation.

### Weaviate Notes (unchanged)

- Existing integration (assumed) provides schema & object handling.
- Need mapping layer for payload parity (e.g., metadata keys).

### Error Handling Strategy

- Wrap backend-specific exceptions into unified exceptions (e.g., `VectorStoreError`).

### Migration / Compatibility

- Add a lightweight schema reconciler that is a no-op for existing collections; for Qdrant, attempts to create collection if missing.

## Health & Observability

- Docker Compose healthcheck now targets Qdrant `/readyz`.
- Future: Add simple `/internal/status` endpoint in Elysia to expose active backend & collection counts.

## Risks

- Feature drift between backends (filters, aggregates) requiring capability negotiation.
- Performance variance; may need adaptive batching per backend.

## Future Enhancements

- Benchmark harness to run identical vector workloads against both backends.
- Caching layer for embedding queries.
- Weaviate adapter implementing the same `VectorDB` interface.
