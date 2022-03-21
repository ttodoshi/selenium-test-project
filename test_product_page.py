from time import sleep


from .pages.product_page import PageObject


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = PageObject(browser, link)
    page.open()
    sleep(3)
    page.add_product_to_basket()
    sleep(3)
    page.success_add_to_basket()
    sleep(3)
    page.product_name_in_basket_is_same_as_product_name()
    sleep(3)
    page.cost_of_the_basket_is_same_as_cost_of_the_product()