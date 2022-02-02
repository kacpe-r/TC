import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from api.groups import delete_all_groups, create_group
from api.users import create_regular_user, delete_user
from config.environment import BASE_URL
from pages.administration import AdministrationPage
from pages.groups import GroupsPage
from pages.header import HeaderPage
from pages.profile import ProfilePage
from steps.login_as_super_user import login_as_super_user
from steps.login_as_user import login_as_user
from utils.group_name import get_group_name
from utils.user_names import get_user_by_role

class TestBase(unittest.TestCase):

    def setUp(self):
        self.service_driver = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service = self.service_driver)
        self.browser.maximize_window()

        regular = get_user_by_role(is_admin = False)
        delete_user(regular['login'])
        create_regular_user(regular['login'])
        self.browser.get(BASE_URL)

    # This test does not use API for creating a new group.
    # It's beneficial to have at least one test that checks creating group with GUI.
    def test_user_not_in_group(self):
        login_as_super_user(self.browser)
            
        header_page = HeaderPage(self.browser)
        header_page.click_administration_link()

        administration_page = AdministrationPage(self.browser)
        administration_page.click_groups_link()

        group_name = get_group_name()
        groups_page = GroupsPage(self.browser)
        groups_page.create_new_group(group_name)

        header_page = HeaderPage(self.browser)
        header_page.log_out()

        login_as_user(self.browser, is_admin = False)

        header_page = HeaderPage(self.browser)
        header_page.go_to_profile()

        profile_page = ProfilePage(self.browser)
        profile_page.click_groups_link()
        
        assert group_name not in profile_page.get_user_groups()

    def test_user_in_group(self):
        user_data = get_user_by_role(is_admin = False)
        group_name = get_group_name()
        create_group(group_name, user_data['login'])

        login_as_user(self.browser, is_admin = False)

        header_page = HeaderPage(self.browser)
        header_page.go_to_profile()

        profile_page = ProfilePage(self.browser)
        profile_page.click_groups_link()

        assert group_name in profile_page.get_user_groups()


    def tearDown(self):
        regular = get_user_by_role(is_admin = False)
        delete_user(regular['login'])
        delete_all_groups()
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
