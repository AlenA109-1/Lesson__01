# Создать класс для страницы авторизации, который будет содержать методы для ввода логина и пароля,
# а также для нажатия кнопки входа.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogPage:

    def __init__(self, driver):
        self.driver = driver
        self.timer = WebDriverWait(driver, 4)

    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def set_autorisation(self):
        self.timer.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#user-name')))  # ожидаем появление любого поля ввода

        self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')  # логин
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')  # пароль

        self.timer.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login-button'))).click() #активность кнопки и нажать




