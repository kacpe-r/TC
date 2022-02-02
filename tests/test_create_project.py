import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.environment import BASE_URL
from pages.administration import AdministrationPage
from pages.create_object import CreateObjectPage
from pages.header import HeaderPage
from pages.overview import OverviewPage
from steps.login_as_super_user import login_as_super_user
from utils.project_name import get_project_name

class TestBase(unittest.TestCase):

    def setUp(self):
        self.service_driver = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service = self.service_driver)
        self.browser.maximize_window()

        self.browser.get(BASE_URL)

        login_as_super_user(self.browser)
            
    def test_create_new_project(self):
        header_page = HeaderPage(self.browser)
        header_page.click_administration_link()

        administration_page = AdministrationPage(self.browser)
        administration_page.click_create_project_button()

        project_name = get_project_name()
        create_object_page = CreateObjectPage(self.browser)
        create_object_page.select_manual_project_creation()
        create_object_page.set_project_name(project_name)
        create_object_page.click_create_button()

        header_page.click_projects_link()

        overview_page = OverviewPage(self.browser)

        assert project_name in overview_page.get_project_names()


    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
