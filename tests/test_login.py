from playwright.sync_api import Page, expect

from pages.home import HomePage
from pages.login import LoginPage


def test_login_navigation_successful(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()

    expect(login_page.login_heading).to_be_visible()

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.successful_login()
    home_page = HomePage(page)

    expect(home_page.home_heading).to_be_visible()