from selenium.webdriver.common.by import By

class LoginPage:
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'loginButton')

    def __init__(self, browser):
        self.browser = browser

    def set_username(self, login):
        username_input = self.browser.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(login)

    def set_password(self, password):
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()
        