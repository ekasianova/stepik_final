from .base_page import BasePage
from .locators import ProductPageLocators
import time

from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_the_basket(self):
        self.should_be_adding_button()
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
        self.solve_quiz_and_get_code()
        time.sleep(2)
        self.slould_be_same_name()
        self.should_be_same_price()
        
    def should_be_adding_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Login field is not presented"
        
    def slould_be_same_name(self):
        productName = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        addedProductName = self.browser.find_element(*ProductPageLocators.ADDED_NAME).text
        assert productName == addedProductName, f"Actual product name{productName}, added{addedProductName}"
        
    def should_be_same_price(self):
        productPrice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        addedProductPrice = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert productPrice == addedProductPrice, f"Actual product name{productPrice}, added{addedProductPrice}"
