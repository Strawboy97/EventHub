import allure


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_heading = page.get_by_role("heading", name="Sign in to EventHub")
        self.email_textbox = page.get_by_role("textbox", name="Email")
        self.password_textbox = page.get_by_role("textbox", name="Password")
        self.sign_in_button = page.get_by_role("button", name="Sign In")
        self.invalid_credentials_toast = page.get_by_text("Invalid email or password", exact=True)

    @allure.step('Navigate to the Login Page')
    def navigate_to_login(self):
        self.page.goto('https://eventhub.rahulshettyacademy.com/login')

    @allure.step('Login to EventHub with {email} and {password}')
    def login(self, email, password):
        self.email_textbox.fill(email)
        self.password_textbox.fill(password)
        self.sign_in_button.click()
