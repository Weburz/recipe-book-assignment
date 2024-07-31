"""Config file to contain fixtures and stuff to test the "product" related routes."""

import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture(scope="package")
def test_client() -> TestClient:
    """Fixture to return an instance of the "TestClient" class as a fixture."""
    return TestClient(app=app)
