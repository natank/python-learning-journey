# Flask Python Server

A simple Flask server written in Python.

## Setup

```bash
pip install -r requirements.txt
```

## Running

```bash
nx serve flask-server
```

Or directly:
```bash
python src/main.py
```

## Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check

## Port

Default: 5000 (configurable via PORT environment variable)
