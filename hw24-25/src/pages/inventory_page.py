from .base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    ITEM_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def add_item_to_cart(self, item_index):

        items = self.driver.find_elements(*self.ITEM_BUTTON)
        items[item_index].click()

    def get_cart_item_count(self):

        cart_badge = self.driver.find_elements(*self.CART_BADGE)
        return int(cart_badge[0].text) if cart_badge else 0
