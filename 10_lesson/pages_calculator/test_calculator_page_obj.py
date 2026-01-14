import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from calculator_page_class import CalculatorPage

import allure

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


@allure.title('Медленный калькулятор')
@allure.description('Проверка результата расчета с задержкой вычисления на 45с')
@allure.feature('Установка параметра ожидания расчета')
@allure.severity('Critical')

def test_02_calc(driver):
    calculator = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator.open_page()

    with allure.step("Задать задержку в ожидании расчетов - 45с"):
        calculator.input_delay()

    with allure.step("Нажать кнопки калькулятора для вычисления  7 + 8 ="):
        calculator.press_calc_buttons()

    with allure.step("Получить результат вычислений"):
        result = calculator.get_result()

    with allure.step("Сравнить результат вычисления с ожидаемым (15)"):
        assert result == '15', f'ожидаемый результат "15", получили "{result}"'

