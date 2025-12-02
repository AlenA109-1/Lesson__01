# Открыть браузер Google Chrome.
# Перейти на страницу: http://uitestingplayground.com/classattr.
# Кликнуть на синюю кнопку.

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

button_locator = 'button.btn-primary'

press_bbutton = driver.find_element(By.CSS_SELECTOR, button_locator)  # возвращает ссылку на элемент

press_bbutton.click() #имитирует клик мышкой
# или search_bbutton.send_keys(Keys.RETURN)
# #имитирует нажатие на Enter, не работает без импорта from selenium.webdriver.common.keys import Keys

sleep(2)