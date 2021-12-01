from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BACKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    
class LoginPageLocators():
    LOGIN_FIELD = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FIELD = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button[value = 'Add to basket']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ADDED_NAME = (By.CSS_SELECTOR, "#messages div.alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages div.alertinner p strong")


class BacketLocators():
    BASKET_SUMMARY = (By.CSS_SELECTOR, "div#content_inner form.basket_summary")
