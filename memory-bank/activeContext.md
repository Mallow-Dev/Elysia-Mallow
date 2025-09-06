# Active Context

## Current Goals (2025-09-06)

1. Launch `elysia` alongside Qdrant via Docker Compose (Qdrant healthcheck now stable on `/readyz`).
2. Add initial tests covering adapter selection and a basic Qdrant upsert/query round trip.
3. Document configuration and operational guidance for switching vector backends.
4. Prepare graceful fallback strategy (optional) if selected backend unavailable.

## Current Blockers

- Elysia container not yet rebuilt/launched post healthcheck fix.

## Immediate Next Action

- Rebuild & start `elysia` container; verify startup with `VECTOR_DB_TYPE=qdrant`.
- Add smoke tests for `QdrantVectorDB` and `QdrantSearch` tool.

## Key Environment Variables

- `VECTOR_DB_TYPE` = one of `weaviate`, `qdrant`
- `QDRANT_URL` = internal service URL (e.g. <http://qdrant:6333>)
- `WEAVIATE_URL` (existing in prior setup, if any) – to be harmonised.

## Open Questions

- Do we need a unified collection/schema migration tool for both backends?
- Will embeddings generation stay identical (so only storage changes) or diverge per backend?

## Risk Notes

- Divergent feature sets (filters, payload structure) may require capability negotiation.
- Potential mismatch in error semantics between backends.

## Progress Update

- Implemented `VectorDB` abstraction with `QdrantVectorDB` and factory (`create_vector_db`) plus env helper (`get_vector_db_from_env`).
- Added `QdrantSearch` tool for basic vector search when `VECTOR_DB_TYPE=qdrant`.
- Docker healthcheck updated to use Qdrant `/readyz` and verified.
- CI added: doc import checks and ruff lint; docs updated to explicit submodule imports.
