import allure
from config import BASE_URL

class RegisterPage:
    def __init__(self, page):
        self.page = page
        self.email_textbox = page.get_by_test_id("register-email")
        self.password_textbox = page.get_by_test_id("register-password")
        self.confirm_password_textbox = page.get_by_role(
            "textbox", name="Repeat your password"
        )
        self.create_account_button = page.get_by_test_id("register-btn")
        self.registration_heading = page.get_by_role(
            "heading", name="Create your account"
        )
        self.email_validation = page.get_by_text("Enter a valid email")
        self.password_empty_validation = page.get_by_text(
            "Password does not meet the requirements below"
        )
        self.password_not_matching_validation = page.get_by_text("Passwords do not match")

    @allure.step("Navigate to Registration")
    def navigate_to_registration(self):
        self.page.goto(f"{BASE_URL}/register")

    @allure.step("Register using {email}, {password} and {confirm_password}")
    def register_new_user(self, email, password, confirm_password):
        self.email_textbox.fill(email)
        self.password_textbox.fill(password)
        self.confirm_password_textbox.fill(confirm_password)
        self.create_account_button.click()
