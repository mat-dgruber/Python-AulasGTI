from fastapi.testclient import TestClient
import sys
import os

# Add the current directory to sys.path to make imports work
sys.path.append(os.getcwd())

try:
    from app_03.main import app
except ImportError:
    # If running from inside app_03, try parent
    sys.path.append(os.path.dirname(os.getcwd()))
    from app_03.main import app

client = TestClient(app)

def test_validation_error():
    # We need a route that triggers validation error.
    # Since we can't easily add a route to the running app instance if it's already compiled/started in some ways,
    # but here we are importing it, so we can add a route.
    
    @app.get("/validation_test/{item_id}")
    def read_item(item_id: int):
        return {"item_id": item_id}

    # Send a string "foo" which is not an integer
    response = client.get("/validation_test/foo")
    
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    
    assert response.status_code == 422
    data = response.json()
    assert data["title"] == "Erro de Validação"
    assert data["type"] == "about:blank"
    # The detail message might vary slightly by pydantic version, but usually contains "Input should be a valid integer"
    print("Validation error response structure verified.")

if __name__ == "__main__":
    try:
        test_validation_error()
        print("Test passed successfully!")
    except Exception as e:
        print(f"Test failed: {e}")
        exit(1)
