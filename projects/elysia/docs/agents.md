# Agents Registry & Standards

This file defines expectations for creating, registering, and maintaining agents in the Elysia codebase.

## Goals

- Consistent agent capabilities & configuration.
- Clear discoverability of available agents.
- Safe execution (bounded, observable, testable).

## Core Concepts

- **Agent**: Named bundle of tools + system prompt + optional config.
- **Tool**: Discrete capability (I/O contract) discoverable via scanning.
- **Agent Manager**: CRUD + registry orchestration.

## Naming Conventions

- Agent names: `snake_case`, concise, capability oriented (e.g., `math_assistant`).
- Tool class names: `PascalCase` ending without generic suffixes (avoid `ToolTool`).
- System prompts: Start with imperative role statement.

## Required Fields

| Field | Description | Rules |
|-------|-------------|-------|
| name | Unique identifier | snake_case, <= 40 chars |
| description | Human-readable purpose | Start with verb or noun phrase |
| tools | List of registered tool names | Must exist in registry |
| system_prompt | Behavioural framing | No secrets or credentials |
| config | Extra settings | JSON-serializable |

## Agent Lifecycle

1. Define required tools (ensure they are registered).
2. Create agent via manager/CLI.
3. Persisted automatically to `agents.json`.
4. Optionally add test covering typical execution path.

## Tool Eligibility Checklist

- [ ] Async `__call__` generator yields `Response` types.
- [ ] Valid `name` (kebab/snake not required but consistent style preferred).
- [ ] Provides `description` (single sentence, present tense).
- [ ] Inputs schema keys have: type, description, required/default.
- [ ] Defensive error handling & clear user-facing messages.

## Execution Safety

- Hard timeouts in executor.
- No unbounded network calls without retries.
- Validate external inputs early.
- Avoid storing secrets in agent definitions.

## Versioning & Changes

- Backwards-incompatible agent schema modifications require a decision log entry.
- Deprecate an agent by marking `deprecated: true` (future field) instead of deleting immediately.

## Observability

- Execution metrics recorded via monitoring dashboard.
- Each agent execution should produce: status, duration, tool usage chain, errors.

## Testing Guidelines

| Scope | What to Test |
|-------|--------------|
| Unit | Tool logic edge cases |
| Integration | Agent execution path with 1–2 tools |
| Regression | Critical bug reproductions remain covered |

## CLI Interaction Examples

```bash
elysia create math_assistant --description "Math operations" --tools SafeMath EnvironmentSummary
elysia execute math_assistant --task "sum 1 2 3"
elysia performance --agent math_assistant
```

## Adding a New Agent (Checklist)

- [ ] Tools exist & are registered.
- [ ] Added via CLI / manager.
- [ ] Added minimal integration test if strategic.
- [ ] Updated documentation (if widely used).
- [ ] No duplication of existing capability without rationale.

## Anti-Patterns

- Overlapping agents differing only by name.
- Tool sprawl without consolidation.
- Embedding business logic inside system prompts instead of tools.

## Future Improvements

- Template-driven guided creation wizard.
- Agent capability diff tool.
- Capability tagging & search.

---
Agents should remain lightweight compositions—not monoliths. Keep responsibilities crisp.
