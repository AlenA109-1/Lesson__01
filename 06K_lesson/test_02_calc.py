import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создайте файл test_02_calc.py и добавьте в него автотест с шагами:
# Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в Google Chrome.
# В поле ввода по локатору #delay введите значение 45.
# Нажмите на кнопки: 7 + 8 =
# Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver # останавливает выполнение фикстуры
    driver.quit()

def test_02_calc(driver):

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    timer = WebDriverWait(driver, 4)
    timer.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#delay')))

    timeout = (driver.find_element(By.CSS_SELECTOR, '#delay'))
    timeout.clear()  # очистит текущее значение
    timeout.send_keys('45')

    timer.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="7"]'))).click() # проверит доступность кнопки и нажмет

    timer.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="+"]'))).click()

    timer.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="8"]'))).click()

    timer.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="="]'))).click()

    timer = WebDriverWait(driver, 45)
    timer.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15'))
    # // div[text() = "15"]
    # // div[@class ="screen"]

    result = driver.find_element(By.CLASS_NAME, 'screen').text.strip()
    assert result == '15', f'ожидаемый результат "15", получили "{result}"'

