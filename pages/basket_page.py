from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HEADER),\
            'You,re not on basket page'
    def check_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE),\
            'Basket is not empty'
    def check_button_to_continue_shopping(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING_LINK),\
            'There is not button to continue shopping'

    def should_not_be_products_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_SUMMARY),\
            'Basket is empty'