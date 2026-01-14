# Создать класс для страницы оформления заказа, который будет содержать методы
# для заполнения формы данными (имя, фамилия, почтовый индекс)
# и проверки итоговой стоимости.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.webdriver import WebDriver
import allure

class OrderPage:
    """Класс содержит методы заполнения персональных данных для заказа и получения итоговой стоимости заказа"""

    def __init__(self, driver: WebDriver) -> None:
        """Метод инициализирует веб-драйвер и задает начальные параметры"""

        self.driver = driver
        self.timer = WebDriverWait(driver, 4)

    @allure.step("Заполнить данные для заказа - имя, фамилия, почтовый индекс")
    def set_pdn(self) -> None:
        """Метод ожидает появления элемента с селектором #first-name, заполняет его (value: str) -  'Alena',
        далее заполняет поля с селекторами #last-name -  'Arkhipova' и #postal-code -  '606120'"""

        self.timer.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#first-name'))).send_keys('Alena')
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Arkhipova')
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('606120')

    @allure.step("Нажать кнопку 'Continue'")
    def press_continue(self) -> None:
        """Метод ожидает появления элемента с селектором #continue и кликает по нему"""

        self.timer.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#continue'))).click()

    @allure.step("Получить итоговую стоимость товаров в корзине")
    def get_total_sum(self) -> float:
        """Метод возвращает итоговую стоимость товаров в корзине - число, тип данных float"""
        sum_cart = self.driver.find_element(By.CLASS_NAME, 'summary_total_label').text
        # найдет элемент с классом summary_total_label, получит из него текст
        sum_cart_value = float(sum_cart.replace('Total: $', ''))
        # заменит символы на пустую строку, тем самым оставит число
        return sum_cart_value