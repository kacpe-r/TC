import time
from selenium.webdriver.common.by import By
from utils.wait_for import wait_for_element_present, wait_for_element_visible

class GroupsPage:
    CREATE_NEW_GROUP_BUTTON = (By.CSS_SELECTOR, '#groupList .addNew')
    GROUP_NAME_INPUT = (By.ID, 'groupName')
    CREATE_GROUP_BUTTON = (By.CSS_SELECTOR, '#addGroupDialog div.popupSaveButtonsBlock > input.submitButton')
    GROUP_NAMES = (By.CSS_SELECTOR, 'table.groupsTable td:nth-of-type(1)')
    FIRST_GROUP_NAME = (By.CSS_SELECTOR, 'table.groupsTable tr:nth-of-type(2) td:nth-of-type(1)')

    def __init__(self, browser):
        self.browser = browser

    def create_new_group(self, group_name):
        wait_for_element_present(self.browser, self.CREATE_NEW_GROUP_BUTTON)

        select_all_users_checkbox = self.browser.find_element(*self.CREATE_NEW_GROUP_BUTTON)
        select_all_users_checkbox.click()

        wait_for_element_present(self.browser, self.GROUP_NAME_INPUT)
        wait_for_element_visible(self.browser, self.GROUP_NAME_INPUT)
        group_name_input = self.browser.find_element(*self.GROUP_NAME_INPUT)
        group_name_input.send_keys(group_name)
        create_group_button = self.browser.find_element(*self.CREATE_GROUP_BUTTON)
        create_group_button.click()

    def open_group_details(self, group_name):
        wait_for_element_present(self.browser, self.FIRST_GROUP_NAME)
        wait_for_element_visible(self.browser, self.FIRST_GROUP_NAME)
        group_names = self.browser.find_elements(*self.GROUP_NAMES)

        for available_group_name in group_names:
            time.sleep(0.5)
            if available_group_name.text == group_name:
                available_group_name.click()
                break

