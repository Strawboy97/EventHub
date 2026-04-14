from playwright.sync_api import Page, expect

from pages.home import HomePage
from pages.login import LoginPage


def test_login_navigation_successful(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()

    expect(login_page.login_heading).to_be_visible()


# Parameterise in future
def test_successful_login(page: Page, read_user_data):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login(read_user_data['email'], read_user_data['password'])
    home_page = HomePage(page)

    expect(home_page.home_heading).to_be_visible()


def test_successful_logout(page: Page, read_user_data):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login(read_user_data['email'], read_user_data['password'])
    home_page = HomePage(page)

    home_page.logout()

    expect(login_page.login_heading).to_be_visible()


def test_incorrect_email_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login('incorrect@email.com', 'incorrect1!')

    expect(login_page.invalid_credentials_toast).to_be_visible()


def test_incorrect_password_login(page: Page, read_user_data):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login(read_user_data['email'], 'incorrect1!')

    expect(login_page.invalid_credentials_toast).to_be_visible()
