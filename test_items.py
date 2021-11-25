import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def test_add_to_cart_button_is_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(15)
    try:
        browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
        isExist = True
    except NoSuchElementException:
        isExist = False
    assert isExist, "No Add to basket button on page"
