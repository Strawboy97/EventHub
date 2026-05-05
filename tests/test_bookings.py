import allure
from playwright.sync_api import Page, expect

from pages.booking import BookingsPage
from pages.home import HomePage


@allure.title("Test Navigation to Bookings Page")
@allure.epic("EventHub")
@allure.feature("UI")
@allure.story("Bookings")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC-BOOKINGS-001")
@allure.label("owner", "Colin M")
def test_successful_navigation(page: Page, login_user):
    home_page = HomePage(page)
    home_page.wait_for_home_page()
    home_page.navigate_to_bookings()

    bookings_page = BookingsPage(page)

    expect(bookings_page.bookings_header).to_be_visible()
