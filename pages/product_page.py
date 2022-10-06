from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def can_add_product_to_basket(self):
        self.can_click_add_product_to_basket()
        self.added_product_correct()
        self.added_product_price_correct()
        
    def can_click_add_product_to_basket(self):
        self.browser.execute_script("window.scrollBy(0,500);")
        #time.sleep(3)
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON),"Button 'Add to busket' does not exist or locator is incorrect"
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()       
##        self.solve_quiz_and_get_code()
        
    def added_product_correct(self):
        time.sleep(3)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_product = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_NAME)
        assert product_name.text == added_product.text, "Added product is not the same as choosen one"
        print(f'Product {product_name.text} added to basket')
        
    def added_product_price_correct(self):
        time.sleep(3)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        added_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_PRICE)
        assert product_price.text == added_product_price.text, "Added product price is not the same as choosen product price"
        print(f'Total price is: {product_price.text}')
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is disappeared, but should not be"    
