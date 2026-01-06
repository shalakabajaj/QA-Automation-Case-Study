# QA Automation Engineering Case Study

## Overview

This project is a **QA Automation Engineering Intern Case Study** that covers:

1. Fixing flaky tests
2. Creating a test automation framework
3. Performing API + UI integration testing

**Technologies Used:**

* Python
* Pytest
* Playwright / Selenium (UI automation)
* Requests (API testing)

---

## Folder Structure

```
QA-Automation-Case-Study/
│
├── config/                  
│   └── config.py            # Configuration file containing URLs, credentials, and environment settings
│
├── docs/                    
│   └── framework_structure.md # Documentation describing the framework design
│
├── pages/                   
│   ├── dashboard_page.py     # Page Object for dashboard UI elements
│   └── login_page.py         # Page Object for login page
│
├── part1_flaky_test_fix/    # Contains fixes for flaky tests (part 1 of case study)
│
├── tests/                   
│   ├── api/                 
│   │   └── test_project_api.py # API test cases for project creation
│   ├── integration/         
│   │   └── test_project_flow.py # End-to-end integration test combining API + UI
│   └── ui/                  
│       └── test_login_ui.py    # UI automation test for login functionality
│
├── utils/                   
│   └── api_client.py         # Utility class for API requests
│
├── .gitignore               # Files and folders to be ignored by Git
├── README.md                # Project overview and instructions
└── requirements.txt         # Python dependencies
```

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/shalakabajaj/QA-Automation-Case-Study.git
cd QA-Automation-Case-Study
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run tests

* **UI Tests:**

```bash
pytest tests/ui/test_login_ui.py
```

* **API Tests:**

```bash
pytest tests/api/test_project_api.py
```

* **Integration Tests:**

```bash
pytest tests/integration/test_project_flow.py
```

### 4. View reports

* Test reports and logs can be saved in a folder of your choice or configured via `config/config.py`.
* Screenshots (if implemented) are generated during UI test execution.

---


## Author

**Shalaka Rajesh Bajaj**
QA Automation Engineering Intern | MCA Student
GitHub: [https://github.com/shalakabajaj](https://github.com/shalakabajaj)
