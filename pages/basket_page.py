from .base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE),\
        "Basket is not empty"       
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
        "Empty basket message is not presented" 
