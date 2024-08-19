#!/usr/bin/env python3
"""The entrypoint script the uvicorn webserver will invoke."""

import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.routes import root, recipe
from src.database import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(root.router)
app.include_router(recipe.router, prefix="/recipes", tags=["recipes"])

def main() -> None:
    """Entrypoint of the script."""
    uvicorn.run("src.main:app", port=8000, host="0.0.0.0", reload=True)  
if __name__ == "__main__":
    main()
