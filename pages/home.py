class HomePage:
    def __init__(self, page):
        self.page = page
        self.home_heading = page.get_by_role(
            "heading", name="Discover & Book Amazing Events"
        )
        self.logout_button = page.get_by_role("button", name="Logout")

    def navigation_check(self):
        self.page.wait_for_url("https://eventhub.rahulshettyacademy.com/")

    def logout(self):
        self.logout_button.click()
