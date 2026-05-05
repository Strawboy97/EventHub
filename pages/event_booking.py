class EventBookingPage:
    def __init__(self, page):
        self.page = page
        self.name_input = page.get_by_role("textbox", name="Full Name*")
        self.email_input = page.get_by_test_id("customer-email")
        self.phone_input = page.get_by_role("textbox", name="Phone Number*")
        self.confirm_button = page.get_by_role("button", name="Confirm Booking")
        self.name_validation = page.get_by_text("Name must be at least 2 chars")
        self.email_validation = page.get_by_text("Enter a valid email")
        self.phone_validation = page.get_by_text("Enter a valid 10-digit phone")
        self.booking_confirmation = page.get_by_text("Your tickets are reserved.")

    def book_event(self, name, email, phone):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.phone_input.fill(phone)

        self.confirm_button.click()
