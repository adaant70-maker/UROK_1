from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_submission():
    driver = webdriver.Chrome()
    # Увеличим таймаут для надежности, раз уж форма на httpbin
    wait = WebDriverWait(driver, 20)

    driver.get("https://httpbin.org/forms/post")
    driver.maximize_window()

    # Работа с полем
    name_field = wait.until(EC.presence_of_element_located((By.NAME, "custname")))
    name_field.clear()
    name_field.send_keys("Диляра")

    previous_url = driver.current_url
  
    # Находим кнопку
    submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit order']")))
    submit_btn.click()
        
    # Ждем, пока URL станет НЕ РАВЕН старому. 
    wait.until(lambda d: d.current_url != previous_url)
    
    new_url = driver.current_url
        
    assert new_url != previous_url, "URL не изменился"
    
    driver.quit()

    
