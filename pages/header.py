import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from utils.wait_for import wait_for_element_visible, wait_for_element_present

class HeaderPage:
    PROJECTS_LINK = (By.CSS_SELECTOR, 'header a[title="Projects"]')
    ADMINISTRATION_LINK = (By.CSS_SELECTOR, 'header a[title="Administration"]')
    AVATAR = (By.CSS_SELECTOR, 'header div[data-hint-container-id="header-user-menu"] > button')
    LOGOUT_LINK = (By.LINK_TEXT, 'Logout')
    PROFILE_LINK = (By.LINK_TEXT, 'Profile')

    def __init__(self, browser):
        self.browser = browser

    def click_administration_link(self):
        wait_for_element_visible(self.browser, self.ADMINISTRATION_LINK)

        administration_link = self.browser.find_element(*self.ADMINISTRATION_LINK)
        administration_link.click()

    def click_projects_link(self):
        wait_for_element_visible(self.browser, self.PROJECTS_LINK)

        projects_link = self.browser.find_element(*self.PROJECTS_LINK)
        projects_link.click()

    def log_out(self):
        self.open_avatar_menu()
        wait_for_element_present(self.browser, self.LOGOUT_LINK)
        wait_for_element_visible(self.browser, self.LOGOUT_LINK)
        logout_link = self.browser.find_element(*self.LOGOUT_LINK)
        logout_link.click()

    def is_administration_link_displayed(self):
        time.sleep(3)
        try:
            self.browser.find_element(*self.ADMINISTRATION_LINK)
        except NoSuchElementException:
            return False
        return True

    def open_avatar_menu(self):
        wait_for_element_present(self.browser, self.AVATAR)
        wait_for_element_visible(self.browser, self.AVATAR)
        avatar = self.browser.find_element(*self.AVATAR)
        avatar.click()

    def go_to_profile(self):
        self.open_avatar_menu()
        wait_for_element_present(self.browser, self.PROFILE_LINK)
        wait_for_element_visible(self.browser, self.PROFILE_LINK)
        profile_link = self.browser.find_element(*self.PROFILE_LINK)
        profile_link.click()
