from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_navigation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)  # Ждём до 15 секунд

    driver.get("https://httpbin.org/")
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT, "HTML form").click()
    
    assert driver.current_url.endswith("/forms/post")
    print(driver.current_url)
    driver.back()
    
    assert driver.current_url == "https://httpbin.org/"
    print(driver.current_url)
   

    driver.quit()