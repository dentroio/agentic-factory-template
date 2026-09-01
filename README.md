# Agentic Factory — product template

**Use this template** (GitHub → Use this template) to get a tiny app plus Work Order stubs. Point the [agentic-factory](https://github.com/dentroio/agentic-factory) **engine** at **this** repo. You do not need any other private product.

| Doc | Purpose |
|-----|---------|
| [SETUP.md](SETUP.md) | Labels, branch protection, optional Actions |
| [PROCESS.md](PROCESS.md) / `AGENT_PROCESS.md` | How agents claim, verify, and open PRs |
| [factory.yaml](factory.yaml) | Verify command, UI URL, patterns — read by the engine |
| [BYO.md](BYO.md) | Replacing `demo/` with a real app |
| Essays | [docs/blog](docs/blog/README.md) |

Engine walkthrough: [Getting Started](https://github.com/dentroio/agentic-factory/blob/main/docs/wiki/Getting-Started.md) · [Product Profile](https://github.com/dentroio/agentic-factory/blob/main/docs/wiki/Product-Profile.md)

## Fast path

1. Create a repo from this template; clone it locally.
2. In a clone of **agentic-factory** (the engine):
   - `make agent-setup` → set `GITHUB_REPO` to `you/this-template-repo`
   - Set `LOCAL_REPO_PATH` in `~/.config/factory-agent/prefs` to the **absolute path** of this product clone
   - `make up` then `make agent-install`
3. Confirm [http://localhost:8099](http://localhost:8099) lists WO-001 … WO-004.
4. An agent claims a WO (`docs/factory/runs/WO-NNN.json`), changes the demo, runs `make ci-local`, asks you to open http://localhost:8765, then opens a PR **here**.

## Demo app

```bash
make run          # http://localhost:8765
make ci-local     # greeting test
```

The visible string lives in `demo/public/index.html`. Sample **WO-001** asks an agent to change it.

`factory.yaml` already points `verify` and `ui_url` at this demo. Edit those fields when you replace the demo with your app.

## Bring your own product

Replace `demo/` with your code. Keep WO paths, claim files, `AGENT_PROCESS.md`, and update `factory.yaml`. Full checklist: [BYO.md](BYO.md) and the engine’s [docs/adopters/BYO.md](https://github.com/dentroio/agentic-factory/blob/main/docs/adopters/BYO.md).

## GitHub

See [SETUP.md](SETUP.md) for labels, branch protection, and optional workflow copies.
