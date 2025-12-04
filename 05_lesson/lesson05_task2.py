# Открыть браузер Google Chrome.
# Перейти на страницу: http://uitestingplayground.com/dynamicid.
# Кликнуть на синюю кнопку.

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

button_locator = '.btn-primary'
# или все тот же - button_locator = 'button.btn-primary'

press_button = driver.find_element(By.CSS_SELECTOR, button_locator).click()

sleep(2)