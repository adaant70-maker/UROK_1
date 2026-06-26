from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_submission():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)  

    try:
        driver.get("https://httpbin.org/forms/post")
        driver.maximize_window()

        
        # Находим поле ввода 
        name_field = wait.until(EC.presence_of_element_located((By.NAME, "custname")))
        name_field.clear()
        name_field.send_keys("Диляра")

        
        # Запоминаем URL до клика
        previous_url = driver.current_url

        # Находим кнопку "Submit"
        submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_btn.click()

        
        # Ждём изменения URL (вместо time.sleep лучше использовать явное ожидание)
        wait.until(lambda d: d.current_url != previous_url)

        # Проверяем, что URL действительно изменился
        new_url = driver.current_url
        assert new_url != previous_url, "URL не изменился после отправки формы"

        
        driver.quit()
