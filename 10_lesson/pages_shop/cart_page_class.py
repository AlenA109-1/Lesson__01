# Создать класс для страницы корзины, который будет содержать методы для нажатия
# кнопки Checkout и проверки содержимого корзины.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.webdriver import WebDriver
import allure

class CartPage:
    """Класс содержит методы проверки добавления товаров в корзину, а также для нажатия кнопки 'Checkout'"""
    def __init__(self, driver: WebDriver) -> None:
        """Метод инициализирует веб-драйвер и задает начальные параметры"""

        self.driver = driver
        self.timer = WebDriverWait(driver, 4)

    @allure.step("Проверить, что в корзине есть товары")
    def check_product(self) -> None:
        """Метод ожидает появления на странице элементов с классом 'inventory_item_name', получает их список, проверяет, что список не пустой"""

        self.timer.until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item_name')))
        list_products = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
        with allure.step("Проверить, что список товаров в корзине не пуст"):
            assert len(list_products) > 0, "Нет ни одного продукта в списке!"

    @allure.step("Нажать кнопку 'Checkout'")
    def press_checkout(self) -> None:
        """Метод ожидает появления кнопки 'Checkout' и кликает по ней"""

        self.timer.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkout'))).click()