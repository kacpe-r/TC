from selenium.webdriver.common.by import By
from utils.wait_for import wait_for_element_present, wait_for_element_visible

class UsersPage:
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'table.usersActions span.addNew')

    def __init__(self, browser):
        self.browser = browser

    def create_admin(self):
        wait_for_element_present(self.browser, self.CREATE_ACCOUNT_BUTTON)
        wait_for_element_visible(self.browser, self.CREATE_ACCOUNT_BUTTON)
        create_account_button = self.browser.find_element(*self.CREATE_ACCOUNT_BUTTON)
        create_account_button.click()
