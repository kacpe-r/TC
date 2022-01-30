from selenium.webdriver.common.by import By

class AdministrationPage:
    MENU_USERS_LINK = (By.LINK_TEXT, 'Users')
    MENU_GROUPS_LINK = (By.LINK_TEXT, 'Groups')
    CREATE_PROJECT_BUTTON = (By.CSS_SELECTOR, '.createProject > a')

    def __init__(self, browser):
        self.browser = browser

    def click_users_link(self):
        menu_users_link = self.browser.find_element(*self.MENU_USERS_LINK)
        menu_users_link.click()

    def click_groups_link(self):
        menu_groups_link = self.browser.find_element(*self.MENU_GROUPS_LINK)
        menu_groups_link.click()

    def click_create_project_button(self):
        create_project_button =  self.browser.find_element(*self.CREATE_PROJECT_BUTTON)
        create_project_button.click()
