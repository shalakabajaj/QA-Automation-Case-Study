import requests
from config.config import BASE_URL

class APIClient:

    def __init__(self, token, tenant_id):
        self.token = token
        self.tenant_id = tenant_id

    def create_project(self, name):
        payload = {
            "name": name,
            "description": "Sample project",
            "team_members": []
        }

        headers = {
            "Authorization": f"Bearer {self.token}",
            "X-Tenant-ID": self.tenant_id
        }

        resp = requests.post(f"{BASE_URL}/api/v1/projects", json=payload, headers=headers)
        return resp.json()
