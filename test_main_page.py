from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link) #инициализируем экземпляр класса и дальше работаем с ним
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser,browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link) #инициализируем экземпляр класса и дальше работаем с ним
    page.open()
    page.go_to_basket_page()
    time.sleep(5)
    basket_page = BasketPage(browser,browser.current_url)
    #1
    basket_page.should_be_empty_basket()
    #2
    basket_page.should_be_empty_basket_message()
  

  
  
