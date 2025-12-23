import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создайте файл test_03_shop.py и добавьте в него автотест с шагами:
# Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
# Авторизуйтесь как пользователь standard_user. secret_sauce
# Добавьте в корзину товары:
# Sauce Labs Backpack., Sauce Labs Bolt T-Shirt., Sauce Labs Onesie.
# Перейдите в корзину.
# Нажмите Checkout.
# Заполните форму своими данными:
# имя, почтовый индекс.
# Нажмите кнопку Continue.
# Прочитайте со страницы итоговую стоимость (Total).
# Закройте браузер.
# Проверьте, что итоговая сумма равна $58.29.

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver # останавливает выполнение фикстуры
    driver.quit()

def test_03_shop(driver):

    driver.get("https://www.saucedemo.com/")

    timer = WebDriverWait(driver, 4)

    timer.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#user-name')))  # ожидаем появление любого поля ввода

    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user') #логин
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce') #пароль

    timer.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login-button'))).click() #активность кнопки и нажать

    timer.until(EC.visibility_of_element_located((By.CLASS_NAME, 'inventory_item_name '))) #карточки товаров

    timer = WebDriverWait(driver, 15)
    timer.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'))).click() # рюкзак

    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()  # черная футболка
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()  # боди

    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click() #перейти в корзину

    timer.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkout'))).click()

    timer.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#first-name'))).send_keys('Alena')
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Arkhipova')
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('606120')

    timer.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#continue'))).click()

   # прочитать (списать) сумму в корзине
    sum_cart = driver.find_element(By.CLASS_NAME, 'summary_total_label').text #найдет элемент с классом summary_total_label, получит из него текст
    sum_cart_value = float(sum_cart.replace('Total: $', '')) #заменит символы на пустую строку, тем самым оставит число
    #print(sum_cart_value) # 58.29

    driver.quit()

    assert sum_cart_value == 58.29, f'Ожидаемое значение суммы товаров в корзине 58.29, отображается {sum_cart_value}'





