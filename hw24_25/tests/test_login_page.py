from pages.login_page import LoginPage
from test_data.user_creds import VALID_CREDENTIALS, INVALID_CREDENTIALS


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_CREDENTIALS["username"], VALID_CREDENTIALS["password"])
    assert "inventory" in driver.current_url, "Login failed for valid credentials"


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(INVALID_CREDENTIALS["username"], INVALID_CREDENTIALS["password"])
    error_message = login_page.find_element(
        "css selector", ".error-message-container"
    ).text
    assert "Epic sadface" in error_message, (
        "Error message not displayed for invalid credentials"
    )
