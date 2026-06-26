from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_multiple_elements():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    
    driver.get("https://httpbin.org/links/10")

    # 1. Ждём, пока на странице появятся все ссылки.
    links = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

    # 2. Проверяем, что их ровно 10 штук.
    assert len(links) == 10

    # 3. Проверяем текст первой ссылки.
    # убираем случайные пробелы по краям, если они есть.
    assert links.text.strip() == "1"

    driver.quit()