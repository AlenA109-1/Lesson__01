# Открыть браузер FireFox. Перейти на страницу: http://the-internet.herokuapp.com/inputs.
# Ввести в поле текст Sky. Очистить это поле (метод clear()).
# Ввести в поле текст Pro. Закрыть браузер (метод quit()).

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox() # открыть браузер

driver.get("http://the-internet.herokuapp.com/inputs")

input_locator = 'input'
input_text = driver.find_element(By.CSS_SELECTOR, input_locator).send_keys('Sky')  # возвращает ссылку на элемент и
# #нажимает кнопки на клавиатуре, соответствующие тексту Sky
sleep(2)

input_text = driver.find_element(By.CSS_SELECTOR, input_locator).clear() #находит поле еще раз по локатору
# и очищает найденное значение

input_text = driver.find_element(By.CSS_SELECTOR, input_locator).send_keys('Pro')
sleep(2)

driver.quit() # закрыть браузер
