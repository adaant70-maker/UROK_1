from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_session_storage_auth():
    driver = None
    try:
        # Инициализация драйвера
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        wait = WebDriverWait(driver, 15)

        # --- БЛОК 1: Работа с Пользователем 1 ---
        
        # Шаг 1. Откройте страницу https://gitflic.ru/
        driver.get("https://gitflic.ru/")

        # Шаг 2. Установите cookie пользователя 1.
        # ВАЖНО: Сначала нужно быть на домене gitflic.ru, чтобы добавить куку.
        # ВСТАВЬ СЮДА значение sessionid (или SESSION) от первого аккаунта
        user1_cookie_value = "ВСТАВИТЬ_VALUE_USER_1" 
        
        if user1_cookie_value != "ВСТАВИТЬ_VALUE_USER_1":
            driver.add_cookie({
                "name": "sessionid",  # Проверь в DevTools точное имя куки (часто sessionid или SESSION)
                "value": user1_cookie_value,
                "domain": "gitflic.ru",
                "path": "/"
            })
        else:
            raise Exception("Ошибка: Не вставлено значение cookie для Пользователя 1!")

        # Шаг 3. Обновите страницу.
        driver.refresh()

        # Шаг 4. Перейдите на страницу пользователя 1.
        # Обычно профиль доступен по ссылке /profile или /username. 
        # Для теста возьмем стандартный путь профиля или главную, если профиль там.
        # Замени 'username1' на реальный логин первого пользователя, если нужно попасть точно в профиль.
        driver.get("https://gitflic.ru/") 
        
        # Небольшая пауза, чтобы страница точно отрисовалась после логина через куку
        wait.until(lambda d: d.current_url is not None)

        # Шаг 5. Сохраните текущий URL.
        url_user1 = driver.current_url
        print(f"URL пользователя 1: {url_user1}")


        # --- БЛОК 2: Работа с Пользователем 2 ---

        # Шаг 6. Разлогиньтесь (очистите куки).
        driver.delete_all_cookies()
        driver.get("https://gitflic.ru/") # Переходим на домен заново, чтобы контекст был чистым

        # Шаг 7. Установите cookie пользователя 2.
        # ВСТАВЬ СЮДА значение sessionid от второго аккаунта
        user2_cookie_value = "ВСТАВИТЬ_VALUE_USER_2"

        if user2_cookie_value != "ВСТАВИТЬ_VALUE_USER_2":
            driver.add_cookie({
                "name": "sessionid",
                "value": user2_cookie_value,
                "domain": "gitflic.ru",
                "path": "/"
            })
        else:
            raise Exception("Ошибка: Не вставлено значение cookie для Пользователя 2!")

        # Шаг 8. Обновите страницу.
        driver.refresh()

        # Шаг 9. Перейдите на страницу пользователя 2.
        # Аналогично шагу 4, можно использовать главную или профиль
        driver.get("https://gitflic.ru/")
        wait.until(lambda d: d.current_url is not None)

        # Шаг 10. Сохраните текущий URL.
        url_user2 = driver.current_url
        print(f"URL пользователя 2: {url_user2}")

        # Финальная проверка: Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
        assert url_user1 != url_user2, f"Ошибка: URL совпали! User1: {url_user1}, User2: {url_user2}"
        print("✅ Тест пройден: URL различаются, авторизация через cookie работает.")
        return True

    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        return False

    finally:
        # САМОЕ ВАЖНОЕ: Гарантированное закрытие браузера
        if driver:
            driver.quit()
            print("Браузер закрыт.")

if __name__ == "__main__":
    result = test_session_storage_auth()
    if result:
        print("🎉 Задача выполнена успешно!")
    else:
        print("😕 Задача не выполнена. Проверь значения cookie и имя поля (sessionid/SESSION).")