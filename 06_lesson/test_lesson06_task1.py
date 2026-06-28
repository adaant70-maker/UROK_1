from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_dynamic_loading():
    driver = webdriver.Chrome()

    try:
        # 1. Откройте страницу
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # 2. Найдите и нажмите на кнопку "Start"
        start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "start"))
        )
        start_button.click()

        # 3. Дождитесь появления текста "Hello World!" 
        WebDriverWait(driver, 30).until(
            EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
        )

        # 4. Сделайте скриншот страницы
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot("screenshots/text_line.png")

        # 5. Проверьте, что появившийся текст равен "Hello World!"
        finish = driver.find_element(By.ID, "finish")
        assert finish.text == "Hello World!"
    finally:
        driver.quit()