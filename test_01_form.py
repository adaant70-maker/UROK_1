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

    print("заполняем поля...")
    
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

    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
