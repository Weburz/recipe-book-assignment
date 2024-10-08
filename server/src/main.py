#!/usr/bin/env python3

"""The entrypoint script the uvicorn webserver will invoke."""

import uvicorn
from fastapi import FastAPI

from src.routes import root

app = FastAPI()

app.include_router(root.router)


def main() -> None:
    """Entrypoint of the script."""
    uvicorn.run("src.main:app", port=8000, host="0.0.0.0", reload=True)  # noqa: S104


if __name__ == "__main__":
    main()
