# Шаги:
# Перейдите на сайт https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
# Дождитесь загрузки всех картинок.
# Получите значение атрибута src у 3-й картинки.
# Выведите значение в консоль.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

timer= WebDriverWait(browser, 10, 0.5) # делать 10 секунд, обновляя запросы через 0,5 секунд

timer.until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, '#text'), 'Done!')) #ждать пока текст не будет равен "Done!"

attr_src = browser.find_element(By.CSS_SELECTOR, '#award').get_attribute('src')
print(attr_src)

browser.quit()


