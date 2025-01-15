FROM python:3.11-slim

WORKDIR /app
RUN pip install poetry
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
COPY README.md README.md
RUN poetry install --no-root
COPY olas_abi.json olas_abi.json
COPY server.py server.py


CMD [ "poetry", "run", "flask", "--debug", "--app", "server.py", "run", "--host", "0.0.0.0", "--port", "8080"]