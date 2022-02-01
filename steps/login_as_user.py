from pages.login import LoginPage
from utils.user_names import get_user_by_role

def login_as_user(browser, is_admin):
    user_data = get_user_by_role(is_admin)
    login_page = LoginPage(browser)
    login_page.set_username(user_data['login'])
    login_page.set_password(user_data['password'])
    login_page.click_login_button()
