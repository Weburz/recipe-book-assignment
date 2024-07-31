"""The test suite for the root route."""

from fastapi.testclient import TestClient


class TestRootRoute:
    """The class to group all test cases for the root route."""

    def test_root_route_returns_status_200_ok(self, test_client: TestClient) -> None:
        """Test whether the root route returns a status code 200 OK."""
        with test_client as client:
            response = client.get("/")
            assert (
                response.status_code == 200
            ), "The root route failed to return a status code 200 OK."
