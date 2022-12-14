from selenium.webdriver.common.by import By
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import pytest


##@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
##                                  ])

##def test_guest_can_add_product_to_basket(browser):
##    #print(f'Test Number {link[-1]}')
##    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
##    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
##    page = BasePage(browser,link) #инициализируем экземпляр класса и дальше работаем с ним
##    page.open()
##    product_page = ProductPage(browser,browser.current_url)
##    product_page.can_add_product_to_basket()
   
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = BasePage(browser,link) #инициализируем экземпляр класса и дальше работаем с ним
    page.open()
    product_page = ProductPage(browser,browser.current_url)
    product_page.can_add_product_to_basket()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = BasePage(browser,link) #инициализируем экземпляр класса и дальше работаем с ним
    page.open()
    product_page = ProductPage(browser,browser.current_url)
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = BasePage(browser,link) #инициализируем экземпляр класса и дальше работаем с ним
    page.open()
    product_page = ProductPage(browser,browser.current_url)
    product_page.can_add_product_to_basket()
    product_page.should_be_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    
@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    time.sleep(5)
    basket_page = BasketPage(browser,browser.current_url)
    #1
    basket_page.should_be_empty_basket()
    #2
    basket_page.should_be_empty_basket_message()
