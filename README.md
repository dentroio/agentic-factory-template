# Agentic Factory — product template

**Use this template** (GitHub → Use this template) to get a tiny app plus Work Order stubs. Point the [agentic-factory](https://github.com/dentroio/agentic-factory) engine at **this** repo. You do not need any other private product.

Process essays: [docs/blog](docs/blog/README.md) (copy of the public series; also in [agentic-factory](https://github.com/dentroio/agentic-factory/tree/main/docs/blog)). Generic process: [PROCESS.md](PROCESS.md) (also `AGENT_PROCESS.md`).

## Fast path

1. Create a repo from this template.
2. In a clone of **agentic-factory** (the engine), run `make agent-setup` and set `GITHUB_REPO` to `you/this-template-repo` (or the dashboard Settings field).
3. Open a sample WO under `docs/project_management/work_orders/`.
4. An agent claims it (`docs/factory/runs/WO-NNN.json`), changes the demo, runs `make ci-local`, asks you to open http://localhost:8765, then opens a PR.

## Demo app

```bash
make run          # http://localhost:8765
make ci-local     # greeting test
```

The visible string lives in `demo/public/index.html`. Sample **WO-001** asks an agent to change it.

## Bring your own product

Replace `demo/` with your code. Keep WO paths, claim files, and `AGENT_PROCESS.md`. Full checklist: in the engine repo, [docs/adopters/BYO.md](https://github.com/dentroio/agentic-factory/blob/main/docs/adopters/BYO.md).

## GitHub

See [SETUP.md](SETUP.md) for labels, branch protection, and optional workflow copies.
