from pages.login_super_user import LoginSuperUserPage
from pages.setup_admin import SetupAdminPage
from pages.login import LoginPage
from utils.super_user import get_super_user

def login_as_super_user(browser):
    super_user_token = get_super_user()

    if 'login.html' in browser.current_url:
        login_page = LoginPage(browser)
        login_page.set_password(super_user_token)
        login_page.click_login_button()
    elif 'setupAdmin.html' in browser.current_url:
        setup_admin_page = SetupAdminPage(browser)
        setup_admin_page.click_login_as_super_user()
        login_super_user_page = LoginSuperUserPage(browser)
        login_super_user_page.set_super_user(super_user_token)
        login_super_user_page.click_login_button()
    else:
        raise ValueError('Unhandled page.')