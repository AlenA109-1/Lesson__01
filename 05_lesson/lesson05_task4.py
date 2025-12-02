# Открыть браузер FireFox. Перейти на страницу http://the-internet.herokuapp.com/login.
# В поле username ввести значение tomsmith. В поле password ввести значение SuperSecretPassword!.
# Нажать кнопку Login.
# Вывести текст с зеленой плашки в консоль. Закрыть браузер (метод quit()).

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox() # открыть браузер

driver.get("http://the-internet.herokuapp.com/login")

# переменные - локаторы
uname_locator = '#username'
password_locator = '#password'
button_locator = 'button.radius'
alert_locator = '#flash'

input_uname = driver.find_element(By.CSS_SELECTOR, uname_locator).send_keys('tomsmith')

input_password = driver.find_element(By.CSS_SELECTOR, password_locator).send_keys('SuperSecretPassword!')

press_button = driver.find_element(By.CSS_SELECTOR, button_locator).click()

sleep(2)

text_alert = driver.find_element(By.CSS_SELECTOR, alert_locator).text # нашел по ИД элемент зеленая строка и на ней ИД текст
print(text_alert)

sleep(2)

driver.quit() # закрыть браузер
