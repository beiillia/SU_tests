from pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
import time

class TestLogin(BaseTest):

    USER_NAME = 'test1'
    USER_PASSWORD = 'test'
    WRONG_USER_NAME = 'qwerty'
    WRONG_USER_PASSWORD = 'Qwe!@#qw$%'

    def test_wrong_username(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(self.WRONG_USER_NAME, self.USER_PASSWORD)
        error_popup_exist = self.loginPage.get_error_login_popup()
        assert error_popup_exist

    def test_wrong_password(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(self.USER_NAME, self.WRONG_USER_PASSWORD)
        error_popup_exist = self.loginPage.get_error_login_popup()
        assert error_popup_exist

    def test_login_wc(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(self.USER_NAME, self.USER_PASSWORD)
        check_client_option_popup = self.loginPage.get_client_option_popup()
        assert check_client_option_popup
        self.loginPage.click_on_ok_proceed_button()
        login_fullname_exist = self.loginPage.get_user_login_fullname()
        assert login_fullname_exist

    def test_logout_wc(self):
        self.test_login_wc()
        self.loginPage.click_on_user_login_fullname()
        self.loginPage.click_on_wc_logout_button()
        check_title_login = self.loginPage.get_title('Serv-U')
        assert check_title_login



#TODO username, pass, hostname - env var

#TODO
#1) inoorrect username
#2) inoorrect pass
#3) succ login
#4) logout


