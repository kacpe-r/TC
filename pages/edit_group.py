from selenium.webdriver.common.by import By
from utils.wait_for import wait_for_element_present, wait_for_element_visible

class EditGroupPage:
    MENU_USERS_LINK = (By.LINK_TEXT, 'Users')
    ADD_USER_TO_GROUP_BUTTON = (By.CSS_SELECTOR, '#groupUsersContainerInner div > a.btn')
    USER_INPUT = (By.ID, 'keyword')
    FILTER_BUTTON = (By.NAME, 'submitFilter')
    USER_CHECKBOX = (By.ID, 'userId') 
    ADD_TO_GROUP_CONFIRM_BUTTON = (By.CSS_SELECTOR, '#attachUsersToGroup .popupSaveButtonsBlock > input.submitButton') 

    def __init__(self, browser):
        self.browser = browser

    def click_users_link(self):
        menu_users_link = self.browser.find_element(*self.MENU_USERS_LINK)
        menu_users_link.click()
    
    def add_user_to_group(self, username):
        add_user_to_group_button = self.browser.find_element(*self.ADD_USER_TO_GROUP_BUTTON)
        add_user_to_group_button.click()
        
        wait_for_element_present(self.browser, self.USER_INPUT)
        wait_for_element_visible(self.browser, self.USER_INPUT)
        user_input = self.browser.find_element(*self.USER_INPUT)
        user_input.send_keys(username)
        filter_button = self.browser.find_element(*self.FILTER_BUTTON)
        filter_button.click()

        wait_for_element_present(self.browser, self.USER_CHECKBOX)
        wait_for_element_visible(self.browser, self.USER_CHECKBOX)
        user_checkbox = self.browser.find_element(*self.USER_CHECKBOX)
        user_checkbox.click()

        add_to_group_confirm_button = self.browser.find_element(*self.ADD_TO_GROUP_CONFIRM_BUTTON)
        add_to_group_confirm_button.click()        
