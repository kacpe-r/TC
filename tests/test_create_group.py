import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.administration import AdministrationPage
from pages.create_user import CreateUserPage
from pages.edit_group import EditGroupPage
from pages.groups import GroupsPage
from pages.header import HeaderPage
from pages.login import LoginPage
from pages.login_super_user import LoginSuperUserPage
from pages.profile import ProfilePage
from pages.setup_admin import SetupAdminPage
from pages.users import UsersPage
from utils.environment import BASE_URL
from utils.group_name import get_group_name
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

        create_user_page = CreateUserPage(self.browser)
        create_user_page.create_new_account()
        
        administration_page.click_groups_link()

    def test_user_not_in_group(self):
        group_name = get_group_name()
        groups_page = GroupsPage(self.browser)
        groups_page.create_new_group(group_name)

        header_page = HeaderPage(self.browser)
        header_page.log_out()

        user_data = get_user_by_role(False)
        login_page = LoginPage(self.browser)
        login_page.set_username(user_data['login'])
        login_page.set_password(user_data['password'])
        login_page.click_login_button()

        header_page = HeaderPage(self.browser)
        header_page.go_to_profile()

        profile_page = ProfilePage(self.browser)
        profile_page.click_groups_link()
        
        assert group_name not in profile_page.get_user_groups()

    def test_user_in_group(self):
        group_name = get_group_name()
        groups_page = GroupsPage(self.browser)
        groups_page.create_new_group(group_name)
        groups_page.open_group_details(group_name)

        user_data = get_user_by_role(False)

        edit_group_page = EditGroupPage(self.browser)
        edit_group_page.click_users_link()
        edit_group_page.add_user_to_group(user_data['login'])

        header_page = HeaderPage(self.browser)
        header_page.log_out()

        login_page = LoginPage(self.browser)
        login_page.set_username(user_data['login'])
        login_page.set_password(user_data['password'])
        login_page.click_login_button()

        header_page = HeaderPage(self.browser)
        header_page.go_to_profile()

        profile_page = ProfilePage(self.browser)
        profile_page.click_groups_link()
        
        assert group_name in profile_page.get_user_groups()


    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
