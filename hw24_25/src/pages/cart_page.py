from .base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEMS)

    def proceed_to_checkout(self):
        self.click_element(*self.CHECKOUT_BUTTON)
