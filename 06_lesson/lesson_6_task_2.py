# Шаги:
# Перейдите на сайт http://uitestingplayground.com/textinput.
# Укажите в поле ввода текст SkyPro.
# Нажмите на синюю кнопку.
# Получите текст кнопки и выведите в консоль ("SkyPro")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/textinput")

browser.find_element(By.CSS_SELECTOR, '#newButtonName').send_keys("SkyPro")

# name_bttn = browser.find_element(By.CSS_SELECTOR, '#updatingButton').text # текущее название кнопки
# print(name_bttn)

browser.find_element(By.CSS_SELECTOR, '#updatingButton').click()

name_bttn = browser.find_element(By.CSS_SELECTOR, '#updatingButton').text # новое название кнопки
print(name_bttn)

browser.quit()