FROM python:3.11-slim

WORKDIR /app
RUN pip install poetry
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
COPY README.md README.md
RUN poetry install --no-root
RUN poetry run pip install --upgrade pip setuptools
COPY olas_abi.json olas_abi.json
COPY server.py server.py

CMD ["poetry",  "run", "waitress-serve", "--call", "server:create_app"]