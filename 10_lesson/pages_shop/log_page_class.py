# Создать класс для страницы авторизации, который будет содержать методы для ввода логина и пароля,
# а также для нажатия кнопки входа.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.webdriver import WebDriver
import allure

class LogPage:
    """Класс содержит методы для ввода логина и пароля, а также для нажатия кнопки входа"""
    def __init__(self, driver : WebDriver) -> None:
        """Метод инициализирует веб-драйвер и задает начальные параметры"""

        self.driver = driver
        self.timer = WebDriverWait(driver, 4)

    @allure.step("Открыть страницу авторизации")
    def open_page(self) -> None:
        """Метод загружает страницу по указанному адресу"""

        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввести логин и пароль (standard_user:secret_sauce), нажать кнопку 'Login'")
    def set_autorisation(self) -> None:
        """Метод ожидает появления на странице элемента с селектором #user-name,
        вводит значение 'standard_user' в поле #user-name, значение 'secret_sauce' в поле #password,
        дожидается появления кнопки с селектором #login-button и кликает по ней"""

        self.timer.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#user-name')))  # ожидаем появление любого поля ввода

        self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')  # логин
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')  # пароль

        self.timer.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login-button'))).click() #активность кнопки и нажать




