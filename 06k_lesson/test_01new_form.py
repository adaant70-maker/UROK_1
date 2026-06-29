import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_validation(driver):
    # 1. Открываем страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)
    wait = WebDriverWait(driver, 15)

        
    # 2. Заполняем все поля 
    wait.until(EC.presence_of_element_located((By.NAME, "first-name"))).send_keys("Иван")
    wait.until(EC.presence_of_element_located((By.NAME, "last-name"))).send_keys("Петров")
    wait.until(EC.presence_of_element_located((By.NAME, "address"))).send_keys("Ленина, 55-3")
    wait.until(EC.presence_of_element_located((By.NAME, "e-mail"))).send_keys("test@skypro.com")
    wait.until(EC.presence_of_element_located((By.NAME, "city"))).send_keys("Москва")
    wait.until(EC.presence_of_element_located((By.NAME, "country"))).send_keys("Россия")
    wait.until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys("+7985899998787")
    wait.until(EC.presence_of_element_located((By.NAME, "job-position"))).send_keys("QA")
    wait.until(EC.presence_of_element_located((By.NAME, "company"))).send_keys("SkyPro")

    # Оставляем Zip пустым
    zip_input = wait.until(EC.presence_of_element_located((By.NAME, "zip-code")))
    zip_input.clear()

     # 3. НАЖИМАЕМ КНОПКУ
    submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_btn.click()

     # --- БЛОК ПРОВЕРОК  ---
    
     # 1. Проверка красного (Zip code)
    error_block = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert-danger[id='zip-code']")))
    text = error_block.text
    assert "N/A" in text or "Не указан" in text, f"Ошибка: ожидалось сообщение об ошибке, а было '{text}'"

    # 2. Проверка зелёного (остальные поля)
    success_fields = [
        "first-name", "last-name", "address", "e-mail", 
        "city", "country", "phone", "job-position", "company"
    ]

    for name in success_fields:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"div.alert-success[id='{name}']")))

    # Вывод 
    print("✅ Все поля заполнены. Проверки пройдены: красный для Zip code и зелёный для остальных полей.")