# Создать класс для страницы корзины, который будет содержать методы для нажатия
# кнопки Checkout и проверки содержимого корзины.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.timer = WebDriverWait(driver, 4)

    def check_product(self):
        self.timer.until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item_name')))
        list_products = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
        assert len(list_products) > 0, "Нет ни одного продукта в списке!"

    def press_checkout(self):
        self.timer.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkout'))).click()