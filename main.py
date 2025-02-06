from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def root():
    res = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
    data = res.json().get("data")
    return {"govos": data}


if __name__ == "__main__":
    import sys

    # If "test" is passed as a command-line argument, run the tests.
    if "test" in sys.argv:
        import unittest
        from fastapi.testclient import TestClient
        from unittest.mock import patch

        # A fake response class to simulate the external API response.
        class FakeResponse:
            def json(self):
                return {"data": [{"Population": 1000000}]}

        class TestRootEndpoint(unittest.TestCase):
            @patch("requests.get")
            def test_root(self, mock_get):
                # Configure the mock to return an instance of FakeResponse.
                mock_get.return_value = FakeResponse()

                # Create a TestClient for the FastAPI app.
                client = TestClient(app)

                # Make a GET request to the root endpoint.
                response = client.get("/")

                # Assert that the status code is 200.
                self.assertEqual(response.status_code, 200)

                # Assert that the JSON response matches our fake data.
                expected_data = [{"Population": 1000000}]
                self.assertEqual(response.json(), expected_data)

        # Run the tests.
        unittest.main(argv=[sys.argv[0]])
    else:
        # Otherwise, run the FastAPI app using Uvicorn.
        import uvicorn

        uvicorn.run(app, host="0.0.0.0", port=8000)
