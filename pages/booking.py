class BookingsPage:
    def __init__(self, page):
        self.page = page
        self.bookings_header = page.get_by_role("heading", name="My Bookings")
