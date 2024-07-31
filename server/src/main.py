#!/usr/bin/env python3

"""The entrypoint script the uvicorn webserver will invoke."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_message() -> dict[str, str]:
    """Return a "Hello World!" JSON message."""
    return {"message": "Hello World!"}
