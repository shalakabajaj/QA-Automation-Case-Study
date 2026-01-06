from utils.api_client import APIClient
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import USERS

def test_project_creation_flow(page):
    # -------- API --------
    api = APIClient(token="dummy_token", tenant_id="company1")
    api_project = api.create_project("UI API Project")

    # -------- UI --------
    login = LoginPage(page)
    dash = DashboardPage(page)

    login.goto()
    login.login(USERS["admin_company1"]["email"], USERS["admin_company1"]["password"])
    dash.wait_for_loaded()

    cards = dash.project_cards()
    assert cards.filter(has_text=api_project["name"]).count() >= 1
