from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

def solution():
    driver = None
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        wait = WebDriverWait(driver, 20)
        
        # 1. Откройте страницу
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # 2. Найдите и нажмите на кнопку "Start"
        start_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button")))
        start_button.click()

        # 3. Дождитесь появления текста "Hello World!"
        hello_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))

        # 4. Сделайте скриншот страницы
        screenshot_path = "dynamic_loading_screenshot.png"
        driver.save_screenshot(screenshot_path)

        # 5. Проверьте, что появившийся текст равен "Hello World!"
        assert hello_element.text == "Hello World!"
        return True

    except Exception:
        return False

    finally:
        # закрывает браузер, выдает результат
        if driver:
            driver.quit()

if __name__ == "__main__":
    result = solution()