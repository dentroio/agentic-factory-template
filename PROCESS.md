# PROCESS.md — generic agent process

Copy kept in sync with [agentic-factory docs/adopters/PROCESS.md](https://github.com/dentroio/agentic-factory/blob/main/docs/adopters/PROCESS.md). Agents in this template repo should follow **this file** (also linked from `AGENT_PROCESS.md`).

---

## Risk tiers

| Tier | Typical work | Human verifies the running product? | Who merges? |
|------|----------------|--------------------------------------|-------------|
| **P0** | Auth, secrets, anything that can leak or lock out | Always | Human |
| **P1** | API contracts, schema, migrations | Always | Human |
| **P2** | Features, UI, most fixes | Yes, then CI | Auto-merge after CI + review LGTM |
| **P3** | Docs / PM markdown only | No | PR required on protected `main` |

One line of application code makes it at least P2. P3 is "no running service is affected."

Dispatch-ready WOs use the canonical shape in `docs/adopters/WO_SPEC_FORMAT.md`: `Problem`, `What to Build`, `Out of scope` or `Do NOT change`, `Acceptance Criteria`, and `Execution`, plus `Priority`, `Effort`, `Services`, and dependencies. Narrative headings in drafts are fine, but normalize them before dispatch.

---

## Work Order flow (P0–P2)

1. Sync `main`.
2. Branch `wo/NNN-short-slug`.
3. **First commit:** `docs/factory/runs/WO-NNN.json` — then push.
4. Implement only what the spec lists.
5. Verify: `make run` and `make ci-local`. For the demo, open http://localhost:8765.
6. **Stop.** Ask a human to confirm the greeting (or your feature) in the browser.
7. Stage explicit paths — never `git add -A`.
8. PR title contains `WO-NNN`.
9. P2: auto-merge after CI + AI review LGTM. P0/P1: human merges.

## Never

- Never commit application code straight to `main`.
- Never `git add -A`.
- Never skip the human checkpoint on P0–P2.
- Never hardcode secrets.
