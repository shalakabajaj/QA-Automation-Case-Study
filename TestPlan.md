QA Automation Case Study – Test Plan (Repo-Specific)

---

1. Introduction
   Purpose:
   Validate the automation framework and scripts in your repo:

* part1_flaky_test_fix/ → Flaky test remediation
* tests/api/test_project_api.py → API test scripts
* tests/ui/test_login_ui.py → UI test scripts
* tests/integration/test_project_flow.py → End-to-end integration tests
* pages/ → Page Object classes (login_page.py, dashboard_page.py)
* config/ → Environment and test data
* utils/api_client.py → Helper functions

Tools Used: Python, Pytest, Playwright, Requests

---

2. Objectives

* Ensure flaky tests in part1_flaky_test_fix/ are stable.
* Validate modular Page Object framework in pages/.
* Ensure API endpoints work as expected via tests/api/test_project_api.py.
* Confirm UI workflows function correctly via tests/ui/test_login_ui.py.
* Test end-to-end integration via tests/integration/test_project_flow.py from API → UI.

---

3. Test Items & Repo References

A. Flaky Test Fixes

* Scripts in part1_flaky_test_fix/
* Validate fixes for Playwright tests
* Add retries/waits as implemented

Acceptance Criteria: Tests pass consistently

B. Framework Validation

* pages/ → login_page.py, dashboard_page.py (Page Object Model)
* config/ → Environment variables, test data
* utils/ → api_client.py helper functions
* tests/ → Proper test structure, naming conventions

C. API Testing

* Scripts: tests/api/test_project_api.py
* Endpoints:

  * POST /api/v1/projects → create project
  * GET /api/v1/projects → fetch projects
  * PUT /api/v1/projects/{id} → update
  * DELETE /api/v1/projects/{id} → delete
* Tenant isolation tested via headers X-Tenant-ID

D. UI Testing

* Scripts: tests/ui/test_login_ui.py
* Validate:

  * Navigation to dashboard
  * UI elements (buttons, input fields)
  * Login flows
  * Visual correctness

E. API + UI Integration Tests

* Scripts: tests/integration/test_project_flow.py
* Steps:

  1. Create project via API (tests/api/test_project_api.py)
  2. Verify project appears in UI (tests/ui/test_login_ui.py checks via Playwright)
  3. Update/delete via API → validate UI update
  4. Tenant isolation enforced

---

4. Test Strategy

* Functional Testing (tests/api/test_project_api.py, tests/ui/test_login_ui.py)
* Regression Testing (all tests in CI)
* Integration Testing (tests/integration/test_project_flow.py)
* Smoke Testing (select critical scripts from tests/)

---

5. Test Data

* config/ folder stores environment and test data
* Includes valid/invalid project payloads, edge cases, random data

---

6. Execution Plan
   | Phase | Folder/Scripts | Duration |
   |-------|----------------|----------|
   | Flaky test fixes | part1_flaky_test_fix/ | 1–2 days |
   | API tests | tests/api/test_project_api.py | 1–2 days |
   | UI tests | tests/ui/test_login_ui.py | 2–3 days |
   | API + UI integration | tests/integration/test_project_flow.py | 1–2 days |
   | Regression & reporting | tests/ + CI logs | 1–2 days |

---

7. Deliverables

* Test Plan doc (this document)
* Test logs (tests/**pycache**/ or CI logs)
* Screenshots from Playwright
* Reports (Allure/JUnit)
