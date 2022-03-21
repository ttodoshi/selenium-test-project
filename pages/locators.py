from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'id_login-username')
    LOGIN_PASSWORD = (By.ID, 'id_login-password')

    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD_CONFIRM = (By.ID, 'id_registration-password2')

class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')

    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, '.alert-success')

    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, '.alert-success strong')

    BASKET_COST = (By.CSS_SELECTOR, '.alert-info strong')
    PRODUCT_COST = (By.CSS_SELECTOR, '.product_main .price_color')