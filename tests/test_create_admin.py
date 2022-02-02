import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from api.users import create_regular_user, delete_user
from config.environment import BASE_URL
from pages.administration import AdministrationPage
from pages.create_user import CreateUserPage
from pages.header import HeaderPage
from pages.users import UsersPage
from steps.login_as_super_user import login_as_super_user
from teamcity_tests.steps.login_as_user import login_as_user
from utils.user_names import get_user_by_role

class TestBase(unittest.TestCase):

    def setUp(self):
        self.service_driver = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service = self.service_driver)
        self.browser.maximize_window()

        self.browser.get(BASE_URL)

        admin = get_user_by_role(is_admin = True)
        regular = get_user_by_role(is_admin = False)
        delete_user(admin['login'])
        delete_user(regular['login'])

    def test_create_new_admin(self):
        login_as_super_user(self.browser)
            
        header_page = HeaderPage(self.browser)
        header_page.click_administration_link()

        administration_page = AdministrationPage(self.browser)
        administration_page.click_users_link()

        users_page = UsersPage(self.browser)
        users_page.create_admin()
        create_user_page = CreateUserPage(self.browser)
        create_user_page.create_new_account(is_admin = True)

        header_page = HeaderPage(self.browser)
        header_page.log_out()

        login_as_user(self.browser, is_admin = True)
        
        assert header_page.is_administration_link_displayed() == True


    def test_create_new_regular_user(self):
        regular = get_user_by_role(is_admin = False)
        create_regular_user(regular['login'])

        header_page = HeaderPage(self.browser)

        login_as_user(self.browser, is_admin = False)

        assert header_page.is_administration_link_displayed() == False

    def tearDown(self):
        admin = get_user_by_role(is_admin = True)
        regular = get_user_by_role(is_admin = False)
        delete_user(admin['login'])
        delete_user(regular['login'])

        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
