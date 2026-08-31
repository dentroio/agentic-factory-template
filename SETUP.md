# GitHub setup (this template repo)

1. **Labels** (Settings → Labels): `new-wo`, `agent-pr`, `pm-sync`.
2. **Branch protection** on `main`: require a pull request; require the **CI** check from `.github/workflows/ci.yml`.
3. **Secrets** (only if you paste extra workflows from the engine’s `templates/github/`):
   - `ANTHROPIC_API_KEY` — planning agent / AI review
   - `GH_PAT` — auto-update PRs so CI retriggers (optional)
4. **Point the factory engine** at this repo (`owner/name`) via `make agent-setup` or dashboard Settings. Do not change the engine’s own GitHub Actions.

Optional paste-ins (into **this** repo only): https://github.com/dentroio/agentic-factory/tree/main/templates/github
