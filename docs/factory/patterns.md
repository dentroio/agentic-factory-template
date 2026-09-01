## Demo app patterns

Follow the existing layout in `demo/`. Do not invent parallel frameworks.

- Greeting / heading text lives in `demo/server.py` (or the file the WO names).
- Keep `make ci-local` green (`make test`).
- Prefer small, reviewable PRs.
