import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создайте файл test_01_form.py и добавьте в него автотест с шагами:
# Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html в Edge или Safari.
# Заполните форму значениями: First name Иван, Last name Петров, Address Ленина, 55-3, Email test@skypro.com,
# Phone number +7985899998787, Zip code *оставить пустым, City Москва, Country Россия, Job position QA,
# Company SkyPro, Нажмите кнопку Submit.
# Проверьте (assert), что поле Zip code подсвечено красным.
# Проверьте (assert), что остальные поля подсвечены зеленым.

@pytest.fixture
def driver():
    # driver = webdriver.Chrome()
    driver = webdriver.Edge(service=EdgeService(r'C:\Users\HOME\Downloads\edgedriver_win64\msedgedriver.exe'))
    driver.maximize_window()
    yield driver # останавливает выполнение фикстуры
    driver.quit()

def test_01_form(driver):

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    timer = WebDriverWait(driver, 4)

    timer.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="first-name"]'))) #ожидаем появление любого поля ввода

    driver.find_element(By.XPATH, '//input[@name="first-name"]').send_keys('Иван') #First name - Иван
    driver.find_element(By.XPATH, '//input[@name="last-name"]').send_keys('Петров') #Last name - Петров
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys('Ленина, 55-3')  #Address - Ленина, 55-3
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys('test@skypro.com') #Email - test@skypro.com
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys('+7985899998787') #Phone number +7985899998787
    # driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys('') #Zip code *оставить пустым
    driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys('Москва') #City - Москва
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys('Россия') #Country - Россия
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys('QA') #Job position - QA
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys('SkyPro') #Company - SkyPro

    timer.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click() #ожидаем активного/кликабельного состояния кнопки, нажимаем

    timer.until(EC.visibility_of_element_located((By.ID, 'zip-code'))) #ожидаем смены локаторов элементов

    zip_code_cls = driver.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute('class')
    assert 'alert py-2 alert-danger' in zip_code_cls, f"Поле zip_code - д.б. красное"  # сравнивает значение атрибута class с заданным значением

    fields_id = ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'city', 'country',
    'job-position', 'company'] #id элементов
    for field in fields_id:
        f_style = driver.find_element(By.ID, field).get_attribute('class')
        assert 'alert py-2 alert-success' == f_style, f"Поле {field} - д.б. зеленое"
