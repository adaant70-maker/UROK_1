from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_form_submission():
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


driver.get("https://httpbin.org/forms/post")
driver.maximize_window()

# Находим поле 
name_field = wait.until(EC.presence_of_element_located((By.NAME, "Custname")))
name_field.clear()
name_field.send_keys("Диляра")

# Запоминаем URL до клика
previous_url = driver.current_url

# Находим кнопку "Submit"
submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
submit_btn.click()

# Ждём перехода
time.sleep(3)

# Проверяем, что URL стал другим
new_url = driver.current_url
assert new_url != previous_url, "URL не изменился"

driver.quit()
