from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from test_data.user_creds import VALID_CREDENTIALS


def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_CREDENTIALS["username"], VALID_CREDENTIALS["password"])

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart(0)
    inventory_page.add_item_to_cart(1)

    assert inventory_page.get_cart_item_count() == 2, "Items were not added to the cart"


def test_cart_checkout(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_CREDENTIALS["username"], VALID_CREDENTIALS["password"])

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart(0)

    driver.find_element("css selector", ".shopping_cart_link").click()
    cart_page = CartPage(driver)

    assert len(cart_page.get_cart_items()) == 1, (
        "Cart does not contain the correct number of items"
    )

    cart_page.proceed_to_checkout()
    assert "checkout-step-one" in driver.current_url, "Failed to navigate to checkout"
