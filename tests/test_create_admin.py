import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.administration import AdministrationPage
from pages.create_user import CreateUserPage
from pages.header import HeaderPage
from pages.login import LoginPage
from pages.login_super_user import LoginSuperUserPage
from pages.setup_admin import SetupAdminPage
from pages.users import UsersPage
from utils.environment import BASE_URL
from utils.super_user import get_super_user
from utils.user_names import get_user_by_role

class TestBase(unittest.TestCase):

    def setUp(self):
        self.service_driver = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service = self.service_driver)
        self.browser.maximize_window()

        self.browser.get(BASE_URL)

        super_user_token = get_super_user()

        if 'login.html' in self.browser.current_url:
            login_page = LoginPage(self.browser)
            login_page.set_password(super_user_token)
            login_page.click_login_button()
        elif 'setupAdmin.html' in self.browser.current_url:
            setup_admin_page = SetupAdminPage(self.browser)
            setup_admin_page.click_login_as_super_user()
            login_super_user_page = LoginSuperUserPage(self.browser)
            login_super_user_page.set_super_user(super_user_token)
            login_super_user_page.click_login_button()
        else:
            raise ValueError('Unhandled page.')
            
        header_page = HeaderPage(self.browser)
        header_page.click_administration_link()

        administration_page = AdministrationPage(self.browser)
        administration_page.click_users_link()

        users_page = UsersPage(self.browser)
        users_page.remove_all_users()
        users_page.create_admin()

    def test_create_new_admin(self):
        create_user_page = CreateUserPage(self.browser)
        create_user_page.create_new_account(True)

        header_page = HeaderPage(self.browser)
        header_page.log_out()

        user_data = get_user_by_role(True)
        login_page = LoginPage(self.browser)
        login_page.set_username(user_data['login'])
        login_page.set_password(user_data['password'])
        login_page.click_login_button()
        
        assert header_page.is_administration_link_displayed() == True


    def test_create_new_regular_user(self):
        create_user_page = CreateUserPage(self.browser)
        create_user_page.create_new_account()

        header_page = HeaderPage(self.browser)
        header_page.log_out()

        user_data = get_user_by_role(False)
        login_page = LoginPage(self.browser)
        login_page.set_username(user_data['login'])
        login_page.set_password(user_data['password'])
        login_page.click_login_button()
        
        assert header_page.is_administration_link_displayed() == False

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
