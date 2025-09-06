# System Patterns

## Architectural Patterns

- Provider / Factory: `get_vector_store()` selects implementation based on configuration.
- Adapter: Each backend implementation adapts native client responses to a unified internal model.
- Tool integration: `QdrantSearch` consumes the abstraction via env-driven factory for minimal coupling.

## Design Patterns

- Strategy Pattern: Backends act as interchangeable strategies for vector operations.
- Facade: Unified interface exposes minimal operations hiding client complexity.

## Common Idioms

- Environment-driven configuration: `VECTOR_DB_TYPE` governs backend selection.
- Graceful degradation: If selected backend unavailable, optionally fallback (planned) after exponential backoff.
- Lightweight imports: Avoid top-level heavy imports; use explicit submodules and optional extras.
