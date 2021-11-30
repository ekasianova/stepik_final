from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    
class LoginPageLocators():
    LOGIN_FIELD = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FIELD = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button[value = 'Add to basket']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ADDED_NAME = (By.CSS_SELECTOR, "#messages div.alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages div.alertinner p strong")
