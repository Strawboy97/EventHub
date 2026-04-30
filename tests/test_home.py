import allure
from playwright.sync_api import Page, expect

from pages.home import HomePage
from pages.login import LoginPage


@allure.title('Test Logo is Displayed')
@allure.epic("EventHub")
@allure.feature("UI")
@allure.story("Home Page")
@allure.severity(allure.severity_level.MINOR)
@allure.testcase('TC-HOME-001')
@allure.label('owner', 'Colin M')
def test_logo_displays(page: Page, login_user):
    home_page = HomePage(page)
    home_page.wait_for_home_page()

    expect(home_page.logo).to_be_visible()


@allure.title('Test Nav Bar Items are Present')
@allure.epic("EventHub")
@allure.feature("UI")
@allure.story("Home Page")
@allure.severity(allure.severity_level.MINOR)
@allure.testcase('TC-HOME-002')
@allure.label('owner', 'Colin M')
def test_all_nav_items_present(page: Page, login_user):
    home_page = HomePage(page)
    home_page.wait_for_home_page()


    expect(home_page.nav_items).to_have_count(6)


@allure.title('Test Home button is Highlighted')
@allure.epic("EventHub")
@allure.feature("UI")
@allure.story("Home Page")
@allure.severity(allure.severity_level.MINOR)
@allure.testcase('TC-HOME-003')
@allure.label('owner', 'Colin M')
def test_home_button_highlight(page: Page, login_user):
    home_page = HomePage(page)
    home_page.wait_for_home_page()

    expect(home_page.home_button).to_contain_class('bg-indigo-50')


@allure.title('Test Logout is Successful')
@allure.epic("EventHub")
@allure.feature("UI")
@allure.story("Home Page")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase('TC-HOME-004')
@allure.label('owner', 'Colin M')
def test_successful_logout(page:Page,login_user):
    home_page = HomePage(page)
    home_page.wait_for_home_page()
    home_page.logout()

    login_page = LoginPage(page)

    expect(login_page.login_heading).to_be_visible()


