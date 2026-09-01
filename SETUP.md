# GitHub setup (this template repo)

1. **Labels** (Settings → Labels): `new-wo`, `agent-pr`, `pm-sync`.
2. **Branch protection** on `main`: require a pull request; require the **CI** check from `.github/workflows/ci.yml`.
3. **Secrets** (only if you paste extra workflows from the engine’s `templates/github/`):
   - `ANTHROPIC_API_KEY` — planning agent / AI review
   - `GH_PAT` — auto-update PRs so CI retriggers (optional)
4. **Point the factory engine** at this repo (`owner/name`) via `make agent-setup` or dashboard Settings.
5. **Local clone path:** in the engine machine’s `~/.config/factory-agent/prefs`, set `LOCAL_REPO_PATH` to this clone’s absolute path. Without it, the dashboard can list WOs but agents cannot implement them.
6. **Product profile:** keep root [`factory.yaml`](factory.yaml) accurate (`verify`, `ui_url`, `patterns_file`). See [Product Profile](https://github.com/dentroio/agentic-factory/blob/main/docs/wiki/Product-Profile.md).

Do **not** change the engine repo’s own GitHub Actions to match this product.

Optional paste-ins (into **this** repo only): https://github.com/dentroio/agentic-factory/tree/main/templates/github
