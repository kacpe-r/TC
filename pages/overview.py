from selenium.webdriver.common.by import By

class OverviewPage:
    PROJECT_NAMES = (By.CSS_SELECTOR, 'table.projectHeaderTable .projectName a')

    def __init__(self, browser):
        self.browser = browser

    def get_project_names(self):
        projects = []
        project_names = self.browser.find_elements(*self.PROJECT_NAMES)

        for project_name in project_names:
            projects.append(project_name.text)

        return projects
