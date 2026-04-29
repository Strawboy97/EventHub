import allure
from playwright.sync_api import Page, expect

from pages.home import HomePage
from pages.register import RegisterPage

@allure.title('Test Successful Navigation to Register Page')
@allure.epic("EventHub")
@allure.feature("Authentication")
@allure.story("User Registration")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase('TC-REGISTER-001')
@allure.label('owner', 'Colin M')
def test_navigation_successful(page: Page):
    register_page = RegisterPage(page)
    register_page.navigate_to_registration()

    expect(register_page.registration_heading).to_be_visible()

@allure.title('Test Validation with Empty Email and Password Fields')
@allure.epic("EventHub")
@allure.feature("Authentication")
@allure.story("User Registration")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.testcase('TC-REGISTER-002')
@allure.label('owner', 'Colin M')
def test_empty_registration_validation(page: Page):
    register_page = RegisterPage(page)
    register_page.navigate_to_registration()
    register_page.register_new_user('', '', '')

    expect(register_page.email_validation).to_be_visible()
    expect(register_page.password_empty_validation).to_be_visible()

@allure.title('Test Validation when Password Fields Do Not Match')
@allure.epic("EventHub")
@allure.feature("Authentication")
@allure.story("User Registration")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.testcase('TC-REGISTER-003')
@allure.label('owner', 'Colin M')
def test_passwords_not_matching(page: Page, create_user_data):
    register_page = RegisterPage(page)
    register_page.navigate_to_registration()
    register_page.register_new_user(create_user_data["email"],
                                                           create_user_data["password"], 'password1!')

    expect(register_page.password_not_matching_validation).to_be_visible()

@allure.title('Test Successful Registration with Valid Email and Password')
@allure.epic("EventHub")
@allure.feature("Authentication")
@allure.story("User Registration")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase('TC-REGISTER-004')
@allure.label('owner', 'Colin M')
def test_successful_registration(page: Page, create_user_data):
    register_page = RegisterPage(page)
    register_page.navigate_to_registration()
    register_page.register_new_user(create_user_data["email"], create_user_data["password"], create_user_data["password"])

    home_page = HomePage(page)
    home_page.wait_for_home_page()

    expect(home_page.home_heading).to_be_visible()
