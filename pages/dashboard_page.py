from playwright.sync_api import Page, expect

class DashboardPage:

    def __init__(self, page: Page):
        self.page = page

    def project_cards(self):
        return self.page.locator(".project-card")

    def wait_for_loaded(self):
        expect(self.page.locator(".welcome-message")).to_be_visible(timeout=8000)
