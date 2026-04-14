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

    def navigate_to_registration(self):
        self.page.goto("https://eventhub.rahulshettyacademy.com/register")

    def click_create_when_fields_empty(self):
        self.create_account_button.click()

    def register_new_user(self, email, password):
        self.email_textbox.fill(email)
        self.password_textbox.fill(password)
        self.confirm_password_textbox.fill(password)
        self.create_account_button.click()

    def click_create_when_passwords_not_matching(self, email, password):
        self.email_textbox.fill(email)
        self.password_textbox.fill(password)
        self.confirm_password_textbox.fill('DiffPassword1!')
        self.create_account_button.click()
