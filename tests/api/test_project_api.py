from utils.api_client import APIClient

def test_create_project_api():
    api = APIClient(token="dummy_token", tenant_id="company1")
    response = api.create_project("API Test Project")

    assert response["name"] == "API Test Project"
