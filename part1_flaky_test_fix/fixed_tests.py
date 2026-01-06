from playwright.sync_api import sync_playwright, expect

def test_user_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Always wait for network to finish
        page.goto("https://app.workflowpro.com/login", wait_until="networkidle")

        page.fill("#email", "admin@company1.com")
        page.fill("#password", "password123")
        page.click("#login-btn")

        # Wait properly for redirect
        expect(page).to_have_url("https://app.workflowpro.com/dashboard", timeout=10000)

        # Dynamic content needs wait
        expect(page.locator(".welcome-message")).to_be_visible(timeout=10000)

        browser.close()


def test_multi_tenant_access():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://app.workflowpro.com/login", wait_until="networkidle")

        page.fill("#email", "user@company2.com")
        page.fill("#password", "password123")
        page.click("#login-btn")

        # Wait for dashboard
        expect(page).to_have_url(lambda url: "dashboard" in url)

        # Wait until project cards load
        cards = page.locator(".project-card")
        expect(cards).to_have_count(1, timeout=15000)

        # Validate company data
        text = cards.first.inner_text()
        assert "Company2" in text

        browser.close()
