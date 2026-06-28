from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def test_cookie_switch():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        base_url = "https://gitflic.ru/"
        driver.get(base_url)

        # --- Пользователь 1 ---
                
        # 1. Добавляем основной SESSION
        cookie_session_1 = {
            "name": "SESSION", 
            "value": "NzEyYjRkOTAtNDU5OS00NTczLWEyMzYtZWFhZjRhMGNhYzBm"  # <-- Вставь сюда значение из колонки "Значение" для SESSION
        }
        
        # 2. Добавляем CSRF-токен (часто требуется для защиты от подделки запросов)
        cookie_csrf_1 = {
            "name": "X-CSRF-TOKEN", 
            "value": "64607051-7ab0-4ab5-9005-dcea934393d3"  # <-- Вставь сюда значение из колонки "Значение" для X-CSRF-TOKEN
        }

        driver.add_cookie(cookie_session_1)
        driver.add_cookie(cookie_csrf_1)

        driver.refresh()
        time.sleep(2)  # Даем время фронтенду обработать сессию

        # Переходим на страницу профиля 
        # Обычно это /profile или /dashboard, либо прямой URL твоего пользователя
        driver.get("https://gitflic.ru/profile") 
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        url_user1 = driver.current_url
        print(f"URL пользователя 1: {url_user1}")

        # --- Разлогин (очистка куки) ---
        driver.delete_all_cookies()

        # --- Пользователь 2 ---
        
        cookie_session_2 = {"name": "SESSION", "value": "ODQ1YTdkYTYtZTFhMi00NDNlLTgyY2UtMTExM2MzYzQxMDg2"}
        cookie_csrf_2 = {"name": "X-CSRF-TOKEN", "value": "6096907c-53de-4b85-8c67-4b9526b208de"}

        driver.add_cookie(cookie_session_2)
        driver.add_cookie(cookie_csrf_2)

        driver.refresh()
        time.sleep(2)

        driver.get("https://gitflic.ru/profile")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        url_user2 = driver.current_url
        print(f"URL пользователя 2: {url_user2}")

        # --- Проверка ---
        assert url_user1 != url_user2, f"URL не различаются: user1={url_user1}, user2={url_user2}"
        print("Тест пройден успешно: URL различаются.")

    finally:
        driver.quit()