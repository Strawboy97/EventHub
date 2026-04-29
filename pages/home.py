import allure
from config import BASE_URL

class HomePage:
    def __init__(self, page):
        self.page = page
        self.logo = page.get_by_role("link", name="EventHub")
        self.nav_bar = page.locator('nav')
        self.nav_items = page.locator('nav .hidden .rounded-lg')
        self.home_button = page.get_by_test_id("nav-home")
        self.home_heading = page.get_by_role(
            "heading", name="Discover & Book Amazing Events"
        )
        self.events_button = page.get_by_test_id("nav-events")
        self.bookings_button = page.get_by_test_id("nav-bookings")
        self.logout_button = page.get_by_role("button", name="Logout")

    @allure.step('Wait for Home Page to Load')
    def wait_for_home_page(self):
        self.page.wait_for_url(f"{BASE_URL}")

    @allure.step('Click the logout Button')
    def logout(self):
        self.logout_button.click()
