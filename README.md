# olas
Server providing market statistics on OLAS


## Installation

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then:

```bash
uv sync --frozen
```

## Run server

You need to set an api key:
```bash
export ALCHEMY_API_KEY=YOUR_KEY
```

Then run the server:
```bash
uv run python server.py
```
