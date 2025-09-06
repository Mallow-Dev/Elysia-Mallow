# Progress

## Done

- [x] Initialize project
- [x] Add Qdrant client dependency & lockfile update
- [x] Create initial Docker Compose with Qdrant + Elysia
- [x] Fix Alpine build issues (psutil / linux headers)
- [x] Implement QdrantSearch tool (basic vector search)
- [x] Fix Qdrant healthcheck (switch to `/readyz`)
- [x] Fixed markdownlint warning and removed duplicate TODO headings in AGENT_MANAGEMENT_README.md
- [x] Created update-memory-bank.md rule in .clinerules to standardize memory bank updates
- [x] Implement vector store abstraction (VectorDB + QdrantVectorDB + factory helpers)
- [x] Add Qdrant healthcheck readiness verification (manual curl to /readyz)

## Doing

- [ ] Rebuild & start `elysia` container with `VECTOR_DB_TYPE=qdrant`
- [ ] Add smoke tests: QdrantVectorDB create/search & QdrantSearch tool integration

## Next

- [ ] Document configuration (README section: Selecting vector backend)
- [ ] Add metrics/perf comparison harness (optional)
- [ ] Implement graceful fallback if chosen backend unavailable
- [ ] Add support for additional vector database backends (Weaviate adapter, others)
- [ ] Explore unified collection/schema migration helper
- [ ] Evaluate embedding pipeline parity & divergence handling
