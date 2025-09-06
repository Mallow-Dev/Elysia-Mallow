# Contributors Guide

Standards and expectations for contributing to the Elysia project.

## Core Principles

- Clarity: Code and docs should be understandable on first read.
- Minimalism: Implement only what is needed—avoid speculative complexity.
- Consistency: Follow existing patterns before inventing new ones.
- Observability: Provide logs or metrics for non-trivial flows.
- Safety: Fail fast with clear errors; avoid silent degradation.

## Branch & Commit Hygiene

| Practice | Requirement |
|----------|------------|
| Branch naming | `feature/<slug>`, `fix/<slug>`, `chore/<slug>` |
| Commit style | Conventional-ish: `feat:`, `fix:`, `chore:`, `docs:`, `refactor:` |
| Commit scope | Small, coherent changes; avoid mixing concerns |
| Rebase | Prefer rebase over merge for PR branches |
| Squash | Squash trivial fixup commits before merge |

## Pull Requests

Checklist before opening a PR:

- [ ] Linked issue or clear standalone rationale
- [ ] Updated / created tests (happy + 1 edge)
- [ ] Updated memory-bank docs if architecture/decisions impacted
- [ ] Ran lint & tests locally (all green)
- [ ] Added/updated type hints where appropriate
- [ ] No stray debug prints or commented-out code

## Code Style

- Use type hints for public functions & class methods.
- Prefer explicit imports (`from elysia.api.vector_db import ...`).
- Keep functions short (<40 lines where practical).
- Avoid global mutable state.
- Validate external inputs and raise well-typed errors.
- Use meaningful variable names; avoid single letters except indices.

## Testing

| Layer | Focus |
|-------|-------|
| Unit | Deterministic logic, edge cases |
| Integration | Tool + environment interactions, vector DB flows |
| CLI | Critical command behaviours |
| Regression | Previously fixed bugs |

Guidelines:

- One assertion concept per test (can check multiple related fields).
- Use factories/builders for repetitive setup.
- Mark network/slow tests with `@pytest.mark.slow`.

## Documentation

- Keep README sections scoped & link deeper docs instead of duplicating.
- Use `decisionLog.md` for major choices; reference dates in architecture notes.
- Update `systemPatterns.md` when adding reusable idioms.

## Performance & Resource Use

- Avoid O(n^2) scans in hot paths without justification.
- Batch external calls where feasible.
- Prefer streaming generators for large result sets.

## Security & Secrets

- Never commit secrets; use env vars.
- Sanitize user-provided prompts/content where reused.
- Treat all external inputs as untrusted.

## Review Expectations

Reviewer should verify:

- Correctness & clarity
- Test adequacy
- No unnecessary abstraction
- Error handling and edge cases addressed
- Memory-bank synchronized

## Deprecation Process

1. Mark feature as deprecated (doc + warning if runtime path used).
2. Provide alternative or migration notes.
3. Remove in a subsequent major/minor as appropriate.

## Anti-Patterns

- Large PRs (>800 LOC diff) without prior design discussion.
- Adding new dependencies without justification in decision log.
- Copy-pasting code instead of extracting a shared utility.
- Hiding complex logic inside a single long function.

## How to Get Started

1. Fork or branch from `main`.
2. Run setup & tests.
3. Make changes following guidelines.
4. Update docs & memory-bank.
5. Open PR with clear summary.

---
Quality scales throughput. Invest in clarity early.
