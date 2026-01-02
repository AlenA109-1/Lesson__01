import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from log_page_class import LogPage
from product_page_class import ProductPage
from cart_page_class import CartPage
from order_page_class import OrderPage

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
    #driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver # останавливает выполнение фикстуры
    driver.quit()

def test_03_shop(driver):
    log_page = LogPage(driver)
    log_page.open_page()
    log_page.set_autorisation()
    product_page = ProductPage(driver)
    product_page.push_to_cart()
    product_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.check_product()
    cart_page.press_checkout()
    order_page = OrderPage(driver)
    order_page.set_pdn()
    order_page.press_continue()
    sum_cart_value = order_page.get_total_sum()

    driver.quit()

    assert sum_cart_value == 58.29, f'Ожидаемое значение суммы товаров в корзине 58.29, отображается {sum_cart_value}'


















