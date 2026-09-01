# Bring your own repo

Full checklist: [engine BYO.md](https://github.com/dentroio/agentic-factory/blob/main/docs/adopters/BYO.md).

Short version:

1. Point the engine’s `GITHUB_REPO` at your app (or keep this template).
2. Set `LOCAL_REPO_PATH` to that app’s local clone.
3. Add `docs/project_management/work_orders/` and `docs/factory/runs/`.
4. Copy `PROCESS.md` → `AGENT_PROCESS.md`.
5. Keep a root [`factory.yaml`](factory.yaml) with your real `verify` / `ui_url` / patterns.
6. Create labels `new-wo`, `agent-pr`, `pm-sync`.

You do not need any other private product.
