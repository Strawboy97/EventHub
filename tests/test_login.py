import allure
from playwright.sync_api import Page, expect

from pages.home import HomePage
from pages.login import LoginPage


@allure.title("Test Successful Navigation to Login Page")
@allure.epic("EventHub")
@allure.feature("Authentication")
@allure.story("User Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC-LOGIN-001")
@allure.label("owner", "Colin M")
def test_login_navigation_successful(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()

    expect(login_page.login_heading).to_be_visible()


# Parameterise in future
@allure.title("Test Login with Correct Email and Password")
@allure.epic("EventHub")
@allure.feature("Authentication")
@allure.story("User Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC-LOGIN-002")
@allure.label("owner", "Colin M")
def test_successful_login(page: Page, read_user_data):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login(read_user_data["email"], read_user_data["password"])
    home_page = HomePage(page)

    expect(home_page.home_heading).to_be_visible()


@allure.title("Test Login Fails using Incorrect Password")
@allure.epic("EventHub")
@allure.feature("Authentication")
@allure.story("User Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC-LOGIN-003")
@allure.label("owner", "Colin M")
def test_incorrect_password_login(page: Page, read_user_data):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login(read_user_data["email"], "incorrect1!")

    expect(login_page.invalid_credentials_toast).to_be_visible()


@allure.title("Test Login fails with Incorrect Email")
@allure.epic("EventHub")
@allure.feature("Authentication")
@allure.story("User Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC-LOGIN-004")
@allure.label("owner", "Colin M")
def test_incorrect_email_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("incorrect@email.com", "incorrect1!")

    expect(login_page.invalid_credentials_toast).to_be_visible()
