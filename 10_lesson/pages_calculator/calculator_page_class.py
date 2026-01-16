from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver


# Создайте файл test_02_calc.py и добавьте в него автотест с шагами:
# Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в Google Chrome.
# В поле ввода по локатору #delay введите значение 45.
# Нажмите на кнопки: 7 + 8 =
# Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.

class CalculatorPage:
    """Этот класс описывает методы взаимодействия с элементами на странице калькулятора"""

    def __init__(self,driver: WebDriver) -> None:
        """Метод инициализирует веб-драйвер и задает начальные параметры"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

        self.data = {
            'delay_input': '45',
            'number': '8',
            'plus': '+',
            'equal': '=',
            'seven': '7'
        }

    def open_page(self) -> None:    #загружает страницу, не возвращает данные
        """Метод загружает страницу по указанному адресу"""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def input_delay(self) -> None:
        """Метод ожидает появления на странице элемента с селектором #delay, очищает в нем данные,
        вводит значение из словаря self.data['delay_input']"""

        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#delay')))
        timeout_element = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        timeout_element.clear()
        timeout_element = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        timeout_element.send_keys(self.data['delay_input']) #вызовет значение из словаря по ключу

    def press_calc_buttons(self) -> None:
        """Метод ожидает появления элементов по XPath, указанным в словаре buttons_selectors, затем кликает по ним"""

        buttons_selectors = {
            'seven': '//span[text()="7"]',
            'plus': '//span[text()="+"]',
            'eight': '//span[text()="8"]',
            'equal': '//span[text()="="]'
        }

        for key, xpath in buttons_selectors.items():
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def get_result(self) -> str:
        """Метод ожидает появления элемента с классом "screen", получает его текст, очищает пробелы и возвращает значение - строку"""

        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15'))
        result = self.driver.find_element(By.CLASS_NAME, 'screen').text.strip()
        return result

