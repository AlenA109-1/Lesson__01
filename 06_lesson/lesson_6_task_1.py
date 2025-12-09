# Шаги:
# Перейдите на страницу http://uitestingplayground.com/ajax.
# Нажмите на синюю кнопку.
# Получите текст из зеленой плашки.
# Выведите его в консоль ("Data loaded with AJAX get request.").

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(17)
browser.get("http://uitestingplayground.com/ajax")

browser.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
green_line = browser.find_element(By.CSS_SELECTOR, '#content')
message = green_line.find_element(By.CSS_SELECTOR, 'p.bg-success').text #вычисляет текст внутри найденного green_line

print(message)

browser.quit()