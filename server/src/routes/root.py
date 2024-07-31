"""The module containing the root route of the server."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_message() -> dict[str, str]:
    """Return a "Hello World!" JSON message."""
    return {"message": "Hello World!"}
