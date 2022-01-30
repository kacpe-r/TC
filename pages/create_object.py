from selenium.webdriver.common.by import By
from utils.wait_for import wait_for_element_visible

class CreateObjectPage:
    MANUAL_CREATION_BUTTON = (By.CSS_SELECTOR, '.menuList_create > a.createOption i.icon-wrench')
    PROJECT_NAME_INPUT = (By.ID, 'name')
    CREATE_PROJECT_BUTTON = (By.ID, 'createProject')

    def __init__(self, browser):
        self.browser = browser

    def select_manual_project_creation(self):
        manual_creation_button = self.browser.find_element(*self.MANUAL_CREATION_BUTTON)
        manual_creation_button.click()

    def set_project_name(self, project_name):
        wait_for_element_visible(self.browser, self.PROJECT_NAME_INPUT)

        project_name_input = self.browser.find_element(*self.PROJECT_NAME_INPUT)
        project_name_input.send_keys(project_name)

    def click_create_button(self):
        create_project_button = self.browser.find_element(*self.CREATE_PROJECT_BUTTON)
        create_project_button.click()
