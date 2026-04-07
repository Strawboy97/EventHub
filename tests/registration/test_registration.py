from playwright.sync_api import Page, expect

from pages.register import RegisterPage


def test_navigation_successful(page: Page):
    register_page = RegisterPage(page)
    register_page.navigate_to_registration()
    expect(register_page.registration_heading).to_be_visible()


def test_empty_registration_validation(page: Page):
    register_page = RegisterPage(page)
    register_page.navigate_to_registration()
    register_page.click_create_when_fields_empty()

    expect(register_page.email_validation).to_be_visible()
    expect(register_page.password_empty_validation)
