
from .base_page import BasePage
from .locators import BacketLocators
import time

from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_be_empty_busket(self):
        assert self.is_not_element_present(*BacketLocators.BASKET_SUMMARY), "Busket summary is presented, but should not be"
