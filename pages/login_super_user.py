from selenium.webdriver.common.by import By

class LoginSuperUserPage:
    SUPER_USER_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'loginButton')

    def __init__(self, browser):
        self.browser = browser

    def set_super_user(self, token):
        super_user_input = self.browser.find_element(*self.SUPER_USER_INPUT)
        super_user_input.send_keys(token)

    def click_login_button(self):
        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()
        