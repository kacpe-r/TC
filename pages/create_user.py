from selenium.webdriver.common.by import By
from utils.user_names import get_user_by_role
from utils.wait_for import wait_for_element_present

class CreateUserPage:
    USERNAME_INPUT = (By.ID, 'input_teamcityUsername')
    PASSWORD_INPUT = (By.ID, 'password1')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'retypedPassword')
    ADMIN_CHECKBOX = (By.CSS_SELECTOR, 'input#administrator')
    CREATE_USER_BUTTON = (By.CSS_SELECTOR, '.saveButtonsBlock input.submitButton')

    def __init__(self, browser):
        self.browser = browser

    def create_new_account(self, is_admin):
        user_data = get_user_by_role(is_admin)
        wait_for_element_present(self.browser, self.USERNAME_INPUT)

        username_input = self.browser.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(user_data['login'])

        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(user_data['password'])

        confirm_password_input = self.browser.find_element(*self.CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(user_data['password'])

        if is_admin:
            admin_checkbox = self.browser.find_element(*self.ADMIN_CHECKBOX)
            admin_checkbox.click()        

        create_user_button = self.browser.find_element(*self.CREATE_USER_BUTTON)
        create_user_button.click()      