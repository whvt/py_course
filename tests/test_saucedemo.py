from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
shopping_items = [
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-bike-light",
    "add-to-cart-sauce-labs-bolt-t-shirt",
    "add-to-cart-sauce-labs-fleece-jacket",
    "add-to-cart-sauce-labs-onesie",
    "add-to-cart-test.allthethings()-t-shirt-(red)",
]

checkout_info = {"first-name": "John", "last-name": "Doe", "postal-code": "12345"}

time.sleep(1)
username.send_keys("standard_user")
time.sleep(1)
password.send_keys("secret_sauce")
time.sleep(1)
login_button.click()


def clicker():
    for item in shopping_items:
        add_to_cart_button = driver.find_element(By.ID, item)
        time.sleep(1)
        add_to_cart_button.click()


clicker()

cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
time.sleep(1)
cart_button.click()


checkout_button = driver.find_element(By.ID, "checkout")
time.sleep(1)
checkout_button.click()


def prompter():
    for key, value in checkout_info.items():
        input_field = driver.find_element(By.ID, key)
        input_field.send_keys(value)
        time.sleep(1)


prompter()

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()


finish_button = driver.find_element(By.ID, "finish")
time.sleep(1)
finish_button.click()


time.sleep(3)
confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header")
time.sleep(3)
driver.quit()
