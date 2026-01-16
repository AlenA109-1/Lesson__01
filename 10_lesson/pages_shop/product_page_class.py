# Создать класс для главной страницы магазина, который будет содержать
# методы для добавления товаров в корзину и перехода в корзину.


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.webdriver import WebDriver
import allure

class ProductPage:
    """Класс содержит методы для выбора и добавления товаров в корзину, затем перехода в корзину"""

    def __init__(self, driver: WebDriver) -> None:
        """Метод инициализирует веб-драйвер и задает начальные параметры"""
        self.driver = driver
        self.timer = WebDriverWait(driver, 15)

    # def open_page(self):
    #     self.driver.get("https://www.saucedemo.com/inventory.html")

    # def push_to_cart(self):
        # self.timer.until(EC.visibility_of_element_located((By.CLASS_NAME, 'inventory_item_name')))  # карточки товаров
        #
        # self.timer.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'))).click()  # рюкзак
        #
        # self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()  # черная футболка
        # self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()  # боди

    @allure.step("Добавить в корзину товары - Sauce Labs Backpack., Sauce Labs Bolt T-Shirt., Sauce Labs Onesie")
    def push_to_cart(self):
        """Метод ожидает появления товаров по селекторам из списка buttons и добавляет их в корзину"""

        self.timer.until(EC.visibility_of_element_located((By.CLASS_NAME, 'inventory_item_name'))) # код предложен Екатериной Никоновой
        buttons = [
                '#add-to-cart-sauce-labs-backpack',
                '#add-to-cart-sauce-labs-bolt-t-shirt',
                '#add-to-cart-sauce-labs-onesie'
                ]
        for btn in buttons:
            self.timer.until(EC.element_to_be_clickable((By.CSS_SELECTOR, btn))).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """Метод осуществляет переход в корзину"""

        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()  # перейти в корзину