from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "'login' is present in the current url"
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email text area is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password text area is not presented"
        # реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email text area is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "Registration password text area is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM), "Registration password confirm text area is not presented"
        # реализуйте проверку, что есть форма регистрации на странице