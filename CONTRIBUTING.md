# Contributing

Thanks for contributing to `olas`.

## Development setup

Prereqs:
- Python 3.10+
- Poetry

Install dependencies:
```bash
poetry install
```

Activate the virtualenv:
```bash
poetry shell
```

## Running locally

This server calls an Ethereum RPC provider via Alchemy. Set:
```bash
export ALCHEMY_API_KEY=YOUR_KEY
```

Run the server:
```bash
python server.py
```

## Code style and checks

CI runs formatting and basic checks. Before opening a PR, run:
```bash
poetry run isort .
poetry run black .
poetry run mypy server.py
```

Optional (not currently enforced in CI):
```bash
poetry run flake8
poetry run pylint server.py
```

## Pull requests

- Keep changes small and focused.
- Update docs (e.g. `README.md`) when behavior or usage changes.
- Do not commit secrets (CI runs gitleaks).

## Security

If you discover a security issue, please avoid filing a public issue. Prefer private disclosure to the maintainers.

