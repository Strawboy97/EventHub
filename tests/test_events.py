import allure
from playwright.sync_api import Page, expect

from pages.event_booking import EventBookingPage
from pages.events import EventPage
from pages.home import HomePage


@allure.title("Test Navigation to Events Page")
@allure.epic("EventHub")
@allure.feature("UI")
@allure.story("Events")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC-EVENTS-001")
@allure.label("owner", "Colin M")
def test_navigation_to_events(page: Page, login_user):
    home_page = HomePage(page)
    home_page.wait_for_home_page()
    home_page.navigate_to_events()

    event_page = EventPage(page)

    expect(event_page.events_heading).to_be_visible()


@allure.title("Test Successful Events Search")
@allure.epic("EventHub")
@allure.feature("Filtering")
@allure.story("Events")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC-EVENTS-002")
@allure.label("owner", "Colin M")
def test_successful_events_search(page: Page, login_user):
    home_page = HomePage(page)
    home_page.wait_for_home_page()
    home_page.navigate_to_events()

    event_page = EventPage(page)
    event_page.search_for_event("World")

    expect(event_page.event_card).to_have_count(1)
    expect(event_page.event_card).to_contain_text("World")


@allure.title("Test Events Search When No Events Found")
@allure.epic("EventHub")
@allure.feature("Filtering")
@allure.story("Events")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC-EVENTS-003")
@allure.label("owner", "Colin M")
def test_events_search_no_events_found(page: Page, login_user):
    home_page = HomePage(page)
    home_page.wait_for_home_page()
    home_page.navigate_to_events()

    event_page = EventPage(page)
    event_page.search_for_event("test")

    expect(event_page.empty_search_heading).to_be_visible()


@allure.title("Test Booking Event")
@allure.epic("EventHub")
@allure.feature("E2E")
@allure.story("Events")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC-EVENTS-004")
@allure.label("owner", "Colin M")
def test_event_booking(page: Page, login_user):
    home_page = HomePage(page)
    home_page.wait_for_home_page()
    home_page.navigate_to_events()

    event_page = EventPage(page)
    event_page.book_now()

    event_booking_page = EventBookingPage(page)
    event_booking_page.book_event("Test User", "test@email.com", "1234567899")

    expect(event_booking_page.booking_confirmation).to_be_visible()
