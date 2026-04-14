class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_heading = page.get_by_role("heading", name="Sign in to EventHub")
        self.email_textbox = page.get_by_role("textbox", name="Email")
        self.password_textbox = page.get_by_role("textbox", name="Password")
        self.sign_in_button = page.get_by_role("button", name="Sign In")

    def navigate_to_login(self):
        self.page.goto('https://eventhub.rahulshettyacademy.com/login')

    def successful_login(self):
        self.email_textbox.fill("parkerbrenda@example.com")
        self.password_textbox.fill("TI%4e1Ir5o")
        self.sign_in_button.click()

