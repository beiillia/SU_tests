from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
BASE_URL = 'https://10.11.43.13'


class LoginPage(BasePage):

    USERNAME_FIELD = (By.ID, 'user-box-text') #TODO rename pass and login button
    PASSWORD_FIELD = (By.ID, 'pword-box-text')
    LOGIN_BUTTON = (By.ID, 'btn-LoginButton')
    WRONG_LOGIN_POPUP = (By.XPATH, '//*[@id="AlertDialogBody"]')
    CLIENT_OPTION_POPUP = (By.ID, 'AskUserPlacementDialogTitleText')
    OK_CONTINUE_OPTION = (By.ID, 'btn-PlacementOKButton')
    USER_LOGIN_FULL_NAME_FIELD = (By.ID, 'UserLogInFullName')
    WC_LOGOUT_BUTTON = (By.XPATH, '//*[@id="SUWCUserOption-logout"]/a')

    def __init__(self, driver):
        super().__init__(driver)  #TODO - no need super
        self.driver.get(BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

#    def is_login_btn_exist(self,):
#        return self.is_visible(self.LOGIN_BUTTON)

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME_FIELD, username)
        self.do_send_keys(self.PASSWORD_FIELD, password)
        self.do_click(self.LOGIN_BUTTON)

    def get_error_login_popup(self):
        return self.WRONG_LOGIN_POPUP

    def get_client_option_popup(self):
        return self.CLIENT_OPTION_POPUP

    def click_on_ok_proceed_button(self):
        return self.do_click(self.OK_CONTINUE_OPTION)

    def get_user_login_fullname(self):
        return self.USER_LOGIN_FULL_NAME_FIELD

    def click_on_user_login_fullname(self):
        return self.do_click(self.USER_LOGIN_FULL_NAME_FIELD)

    def click_on_wc_logout_button(self):
        return self.do_click(self.WC_LOGOUT_BUTTON)


