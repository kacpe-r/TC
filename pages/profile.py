from selenium.webdriver.common.by import By

class ProfilePage:
    MENU_GROUPS_LINK = (By.LINK_TEXT, 'Groups')
    GROUP_NAMES = (By.CSS_SELECTOR, 'table.settings.userProfileTable td:nth-of-type(1)')

    def __init__(self, browser):
        self.browser = browser

    def click_groups_link(self):
        menu_groups_link = self.browser.find_element(*self.MENU_GROUPS_LINK)
        menu_groups_link.click()

    def get_user_groups(self):
        groups = []
        group_names = self.browser.find_elements(*self.GROUP_NAMES)
        for group_name in group_names:
            groups.append(group_name.text)

        return groups
