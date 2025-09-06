# Mono-repo Restructure Move Plan

## Move to projects/elysia/

- elysia/ → projects/elysia/
- AGENT_MANAGEMENT_README.md → projects/elysia/docs/agent_management.md
- AGENTS.md → projects/elysia/docs/agents.md
- CONTRIBUTORS.md → projects/elysia/CONTRIBUTING.md (merge if duplicate)
- ELYSIA_CODEX_JOB_SPEC.md → projects/elysia/docs/ELYSIA_CODEX_JOB_SPEC.md
- example_job_spec.json → projects/elysia/examples/example_job_spec.json
- job_executor_example.py → projects/elysia/examples/job_executor_example.py
- resources.txt → projects/elysia/docs/resources.md
- agents.json → projects/elysia/agents.json

## Keep at repo root

- docker/
- memory-bank/
- Qdrant/
- .env
- tests/
- cspell.config.yaml

## Archive (repo-archive/)

- Any duplicates or unknown files after review

## Notes

- Update all references in docs, CI, Docker, and tests to new paths.
- Update memory-bank entries to document the restructure.
- Create VSCode workspace file at repo root.
