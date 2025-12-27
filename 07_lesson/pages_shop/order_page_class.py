# Создать класс для страницы оформления заказа, который будет содержать методы
# для заполнения формы данными (имя, фамилия, почтовый индекс)
# и проверки итоговой стоимости.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage():
    def __init__(self, driver):
        self.driver = driver
        self.timer = WebDriverWait(driver, 4)

    def set_pdn(self):
        self.timer.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#first-name'))).send_keys('Alena')
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Arkhipova')
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('606120')

    def press_continue(self):
        self.timer.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#continue'))).click()

    def get_total_sum(self):
        sum_cart = self.driver.find_element(By.CLASS_NAME, 'summary_total_label').text
        # найдет элемент с классом summary_total_label, получит из него текст
        sum_cart_value = float(sum_cart.replace('Total: $', ''))
        # заменит символы на пустую строку, тем самым оставит число
        return sum_cart_value