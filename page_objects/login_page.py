from selenium.webdriver.common.by import By
from utils.web_ui.base_page import BasePage


class LoginPage(BasePage):
    __login_input = (By.ID, "form3-username")
    __password_input = (By.ID, "form3-password")
    __sign_in_button = (By.XPATH, "//div[@class ='one-factor']/button[@class ='submit button']")
    __auth_login_box = (By.XPATH, "//main[@class = 'auth auth-login box box-pad']")

    def __init__(self, driver):
        super().__init__(driver)

    def set_user_login(self, email):
        self.send_keys(self.__login_input, email)
        return self

    def set_password(self, password):
        self.send_keys(self.__password_input, password)
        return self

    def click_sign_in_button(self):
        self.click(self.__sign_in_button)
        return self

    def sign_in(self, email, password):
        self.set_user_login(email)
        self.set_password(password)
        self.click_sign_in_button()

    def auth_login_box_label(self):
        return self.__auth_login_box

    def auth_login_box_label_invisibility(self):
        self.wait_for_element_invisibility(self.__auth_login_box)
        return self

