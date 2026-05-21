# Contributing

Thanks for contributing to `olas`.

## Development setup

Prereqs:
- Python 3.10+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Install dependencies (runtime + dev tools):
```bash
uv sync --frozen
```

`uv` manages the venv at `./.venv`; activate it with `source .venv/bin/activate`, or just prefix commands with `uv run`.

## Running locally

This server calls an Ethereum RPC provider via Alchemy. Set:
```bash
export ALCHEMY_API_KEY=YOUR_KEY
```

Run the server:
```bash
uv run python server.py
```

## Code style and checks

CI runs formatting and basic checks. Before opening a PR, run:
```bash
uv run isort .
uv run black .
uv run mypy server.py
```

Optional (not currently enforced in CI):
```bash
uv run flake8
uv run pylint server.py
```

## Pull requests

- Keep changes small and focused.
- Update docs (e.g. `README.md`) when behavior or usage changes.
- Do not commit secrets (CI runs gitleaks).

## Security

If you discover a security issue, please avoid filing a public issue. Prefer private disclosure to the maintainers.

