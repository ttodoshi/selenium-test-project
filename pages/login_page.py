from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url,\
            "'login' is present in the current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL),\
            "Login email text area is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD),\
            "Login password text area is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL),\
            "Registration email text area is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD),\
            "Registration password text area is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM),\
            "Registration password confirm text area is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_confirm_input.send_keys(password)
        confirm_register = self.browser.find_element(*LoginPageLocators.REGISTER_USER)
        confirm_register.click()
        self.should_be_authorized_user()