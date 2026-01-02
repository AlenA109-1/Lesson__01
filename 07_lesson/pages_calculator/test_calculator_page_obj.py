import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from calculator_page_class import CalculatorPage

# Создайте файл test_02_calc.py и добавьте в него автотест с шагами:
# Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в Google Chrome.
# В поле ввода по локатору #delay введите значение 45.
# Нажмите на кнопки: 7 + 8 =
# Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver # останавливает выполнение фикстуры
    driver.quit()

def test_02_calc(driver):

    calculator = CalculatorPage(driver)
    calculator.open_page()
    calculator.input_delay()
    calculator.press_calc_buttons()
    result = calculator.get_result()

    assert result == '15', f'ожидаемый результат "15", получили "{result}"'

