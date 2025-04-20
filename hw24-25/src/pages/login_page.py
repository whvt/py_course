from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def enter_username(self, username):
        self.send_keys(*self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.send_keys(*self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(*self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
