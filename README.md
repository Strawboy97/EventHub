# EventHub Test Framework

An end-to-end UI test automation framework for the EventHub web application, built with **Playwright**, **pytest**, and **Allure** reporting.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| [Playwright](https://playwright.dev/python/) | Browser automation |
| [pytest](https://docs.pytest.org/) | Test runner |
| [Allure](https://docs.qameta.io/allure/) | Test reporting |
| [pytest-faker](https://pypi.org/project/pytest-faker/) | Dynamic test data generation |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## Project Structure

```
├── pages/                  # Page Object Model classes
│   ├── booking.py
│   ├── event_booking.py
│   ├── events.py
│   ├── home.py
│   ├── login.py
│   └── register.py
├── tests/                  # Test files
│   ├── test_bookings.py
│   ├── test_events.py
│   ├── test_home.py
│   ├── test_login.py
│   └── test_registration.py
├── config.py               # Environment configuration
├── conftest.py             # Shared pytest fixtures
├── userData.json           # Persistent test user data
├── pytest.ini              # pytest configuration
└── .env.sample             # Environment variables
```

---

## Prerequisites

- Python 3.8+
- [Allure CLI](https://docs.qameta.io/allure/#_installing_a_commandline) installed and on your PATH

---

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/Strawboy97/EventHub.git
cd EventHub
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Install Playwright browsers**
```bash
playwright install
```

**5. Configure environment variables**

Create a `.env` file in the project root:
```
BASE_URL=https://your-eventhub-url.com
```

> ⚠️ Never commit your `.env` file. It is included in `.gitignore`.

---

## Running the Tests

**Run all tests**
```bash
pytest
```

**Run a specific test file**
```bash
pytest tests/test_login.py
```

**Run a specific test**
```bash
pytest tests/test_login.py::test_successful_login
```

**Run in headed mode (see the browser)**
```bash
pytest --headed
```

**Run with a specific browser**
```bash
pytest --browser firefox
```

---

## Viewing the Allure Report

After running tests, an `allure-results/` directory will be generated. To view the report:

**Serve the report locally**
```bash
allure serve allure-results
```

**Or generate a static report**
```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

---

## Test Coverage

| Area | Tests |
|------|-------|
| Authentication — Login | Navigation, successful login, incorrect password, incorrect email |
| Authentication — Registration | Navigation, empty field validation, password mismatch, successful registration |
| Home Page | Logo display, nav bar items, active nav highlight, logout |
| Events | Navigation, search with results, search with no results, full booking flow |
| Bookings | Navigation to bookings page |

---

## Test Data

User credentials are stored in `userData.json`. New users created during registration tests are automatically appended to this file via the `create_user_data` fixture.

> The first entry in `userData.json` is used as the default login user for tests that require authentication.

---

## Key Design Decisions

- **Page Object Model (POM)** — All locators and page interactions are encapsulated in page classes under `pages/`, keeping tests clean and maintainable.
- **Allure integration** — Tests are annotated with epic, feature, story, severity, and owner metadata for rich reporting.
- **Fixture-based login** — The `login_user` fixture handles authentication as a precondition, avoiding repetition across tests.
