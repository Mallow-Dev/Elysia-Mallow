# Memory Bank Guidelines

This directory captures evolving project knowledge. Keep it concise, factual, and synchronized with code changes.

## Files

| File | Purpose |
|------|---------|
| `projectBrief.md` | High-level purpose & scope. Update only on strategic shifts. |
| `productContext.md` | Product framing, users, value, core features. Keep current with roadmap pivots. |
| `architect.md` | Architecture & interface contracts. Update when introducing or altering components. |
| `systemPatterns.md` | Reusable patterns & idioms adopted in the codebase. |
| `decisionLog.md` | Immutable chronological record of significant decisions. Never rewrite history—append only. |
| `activeContext.md` | Snapshot of current goals, blockers, next actions (short horizon). Update freely. |
| `progress.md` | Kanban-style Done / Doing / Next reflecting actionable tasks. |

## Update Principles

1. Source of Truth: Code > memory-bank. Docs must reflect implemented reality. Mark speculative ideas as such.
2. Minimal Drift: Update affected files as part of the same commit / PR that changes code.
3. Atomic Decisions: One decision per row in `decisionLog.md` with clear rationale.
4. Temporal Accuracy: `activeContext.md` is present tense; `progress.md` uses past tense for Done, imperative for Doing/Next.
5. No Duplicates: A task appears only once (prefer `progress.md`). Broader strategic goals can live in `activeContext.md`.
6. Traceability: Architecture changes should reference decision log entries (by date) if they stem from explicit decisions.
7. Brevity Over Narrative: Use bullets, avoid prose bloat. 3–7 bullet limits per section where practical.
8. Status Integrity: Move items left-to-right: Next → Doing → Done. Never regress without note.
9. Append-Only Decisions: Don’t edit historical `decisionLog` rows—add a superseding decision instead.
10. Consistent Terminology: Use the same names for components, env vars, and interfaces as in code.

## Workflow Expectations

- When adding a new component/interface: update `architect.md`, add a decision if non-trivial, optionally add pattern if reusable.
- When removing / deprecating: mark previous decision as superseded (new row) and update affected docs.
- After shipping a feature: reflect in `progress.md` (Done) and, if architectural, ensure `architect.md` is updated.
- Before starting work: confirm `activeContext.md` goals align with `progress.md` Doing column.

## Anti-Patterns (Avoid)

- Leaving stale blockers after they are resolved.
- Duplicating the same task in multiple files.
- Mixing speculative future ideas into `decisionLog.md` (belongs in roadmap backlog elsewhere).
- Long narrative paragraphs—harder to diff and maintain.

## Review Checklist (Pre-Commit)

- [ ] Does code introduce/remove a component? Update `architect.md`.
- [ ] Did we choose between alternatives? Add to `decisionLog.md`.
- [ ] Are current goals/blockers still accurate? Refresh `activeContext.md`.
- [ ] Was progress state updated (Done/Doing/Next)?
- [ ] Any new reusable patterns? Add to `systemPatterns.md`.
- [ ] Are env vars documented consistently?

## Style

- Markdown, headings start at level 1 per file.
- Use backticks for code identifiers and env vars.
- Wrap lines at ~100 chars where reasonable.
- Use ISO dates (YYYY-MM-DD).

## Tooling Ideas (Optional Future)

- Lint to ensure decision log rows aren't edited.
- Script to diff code symbols vs documented architecture for drift.
- CI check: ensure `progress.md` Doing not empty for active branches.

---
Maintain discipline here and future contributors (human or AI) ramp faster with fewer missteps.
