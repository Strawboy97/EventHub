class EventPage:
    def __init__(self, page):
        self.page = page
        self.events_heading = page.get_by_role("heading", name="Upcoming Events")
        self.empty_search_heading = page.get_by_role("heading", name="No events found")
        self.search_box = page.get_by_role("textbox", name="Search events, venues…")
        self.event_card = page.get_by_test_id("event-card")

    def search_for_event(self, event_name:str):
        self.search_box.fill(event_name)
