from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import USERS

def test_login_success(page):
    login = LoginPage(page)
    dash = DashboardPage(page)

    login.goto()
    login.login(USERS["admin_company1"]["email"], USERS["admin_company1"]["password"])
    dash.wait_for_loaded()
