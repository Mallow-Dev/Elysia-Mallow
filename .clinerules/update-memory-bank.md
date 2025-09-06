# Elysia - Mallow Repository Memory Bank (Repo-specific)

This file documents the memory-bank for the Elysia - Mallow repository. Use it for repository-scoped context, decisions, and status that affect agents, CI, runtime, and contributors working on this repo.

Location: .clinerules/global-memory-bank.md (repository-local)

Purpose:

- Keep all repo maintainers and automation agents in sync with changes to goals, architecture, workflows, and environment variables specific to Elysia - Mallow.
- Limit entries here to repository-impacting changes (not organization-wide policies).

Memory-Bank Areas (repo files to keep up-to-date)

- activeContext.md: Current repo goals, blockers, next actions, env vars (e.g., VECTOR_DB_TYPE, DB_CONNECTION), open questions, and progress relevant to Elysia - Mallow.
  - Update when priorities, blockers, or environment values change for this repo.
- architect.md: Repo-specific architectural decisions, interfaces, migration plans, observability rules, and technical debt items.
  - Update when we change service boundaries, data stores, or major integrations used by this repo.
- decisionLog.md: Key repository decisions, rationale, and references to PRs/issues.
  - Update for every non-trivial decision that will affect maintenance, deployments, or agent behavior in this repo.
- productContext.md: Requirements and user-context for features implemented in this repository.
  - Update when feature scope or acceptance criteria change for repo deliverables.
- progress.md: Task status for repo issues/PRs, sprint items, and handoff notes.
  - Update after each significant task state change for repo work.
- projectBrief.md: Short repo summary, goals for the next milestones, and owners.
  - Update when milestone scope or owners change.
- systemPatterns.md: Conventions, code patterns, and infra practices adopted in this repo (linting, testing, release flow).
  - Update when new conventions or release steps are introduced.

When to Update (repo scope)

- After any code, config, or architecture change within this repo.
- When repo-level decisions are made that affect CI, agents, or deployment.
- When blockers are resolved, new risks identified, or goals shift for Elysia - Mallow.
- After onboarding new contributors to this repository.
- Whenever any repo memory area becomes outdated.

Why Update (repo scope)

- Ensures contributors and automation working on this repository have current context.
- Preserves traceability for repo-specific decisions and rollout rationale.
- Speeds onboarding and reduces duplicate work for repo contributors.

Minimal Entry Template (use for this repo)

- Date: YYYY-MM-DD
- Area: (activeContext, architect, decisionLog, etc.)
- Change Summary: What changed, why, and PR/issue reference.
- Impact: Who/what in this repo is affected (services, agents, CI jobs).
- Migration/Action: Steps required (if any) to apply the change in this repo.

Example Entry

- Date: 2025-09-06
- Area: decisionLog
- Change Summary: Adopted Qdrant for local dev embeddings in Elysia - Mallow; added VECTOR_DB_TYPE env var and VectorDB adapter; updated README for local setup.
- Impact: Local dev agents and CI jobs using vector search; update dev environment docs and CI secrets.

Contributor Checklist (repo)

- [ ] Review all repo memory-bank areas for relevance to this change.
- [ ] Create an entry using the minimal template with links to PRs/issues.
- [ ] Update related files (README, env docs, CI) referenced in the entry.
- [ ] Mention any required follow-up tasks in progress.md and create issues if needed.

Other Repo Guidelines

- Only record repo-scoped changes here; cross-repo or org-wide policies belong elsewhere.
- Record rollbacks and feature toggles as explicit entries with rationale.
- Keep entries concise and include links to PRs/issues for detail.
- Enforce this workflow for every merged PR that materially changes repo behavior.
