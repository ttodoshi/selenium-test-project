from selenium_test_project.pages.base_page import BasePage
from .locators import ProductPageLocators


class PageObject(BasePage):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def success_add_to_basket(self):
        success_add_to_basket_message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET).text
        assert success_add_to_basket_message, 'Товар не добавлен в корзину'

    def product_name_in_basket_is_same_as_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name == product_name_in_basket, 'Добавлен неверный товар'

    def cost_of_the_basket_is_same_as_cost_of_the_product(self):
        cost_of_the_basket = self.browser.find_element(*ProductPageLocators.BASKET_COST).text
        cost_of_the_product = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        assert cost_of_the_basket == cost_of_the_product, 'Стоимость корзины и товара различается, возможно товар не добавлен в корзину'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"