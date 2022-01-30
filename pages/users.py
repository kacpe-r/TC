from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.wait_for import wait_for_element_to_be_clickable, wait_for_element_present, wait_for_element_visible

class UsersPage:
    SELECT_ALL_USERS_CHECKBOX = (By.ID, 'selectAll')
    USERS_ACTION_BUTTONS = (By.CSS_SELECTOR, '.users-operations > a')
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'table.usersActions span.addNew')

    def __init__(self, browser):
        self.browser = browser

    def remove_all_users(self):
        select_all_users_checkbox = self.browser.find_element(*self.SELECT_ALL_USERS_CHECKBOX)
        select_all_users_checkbox.click()

        user_action_buttons = self.browser.find_elements(*self.USERS_ACTION_BUTTONS)

        for user_action in user_action_buttons:
            if user_action.get_attribute("text") == "Remove users":
                wait_for_element_to_be_clickable(self.browser, user_action)
                user_action.click()

        try:
            WebDriverWait(self.browser, 3).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass

    def create_admin(self):
        wait_for_element_present(self.browser, self.CREATE_ACCOUNT_BUTTON)
        wait_for_element_visible(self.browser, self.CREATE_ACCOUNT_BUTTON)
        create_account_button = self.browser.find_element(*self.CREATE_ACCOUNT_BUTTON)
        create_account_button.click()
