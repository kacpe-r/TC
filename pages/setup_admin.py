from selenium.webdriver.common.by import By

class SetupAdminPage:
    LOGIN_SUPER_USER_LINK = (By.LINK_TEXT, 'Login as Super user')

    def __init__(self, browser):
        self.browser = browser

    def click_login_as_super_user(self):
        submit_button = self.browser.find_element(*self.LOGIN_SUPER_USER_LINK)
        submit_button.click()
        