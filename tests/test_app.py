from app import app
import json

def test_json_response():
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert json.loads(response.data)  # Test if response is JSON parsable
