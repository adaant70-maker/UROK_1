import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shop_purchase_flow(driver):
    wait = WebDriverWait(driver, 15)
    url = "https://www.saucedemo.com/"
    
    driver.get(url)
    
    # --- АВТОРИЗАЦИЯ ---
    wait.until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Ждем загрузки списка товаров
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))

    # --- ДОБАВЛЕНИЕ ТОВАРОВ ---
    # Список ID кнопок для нужных товаров
    cart_items_ids = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    
    # Проходимся по каждому товару
    for index, item_id in enumerate(cart_items_ids):
        # 1. Находим кнопку и кликаем
        btn = wait.until(EC.element_to_be_clickable((By.ID, item_id)))
        btn.click()
        
        # 2. Ждем, пока счетчик в корзине обновится
        # Ожидаем, что в корзине станет (index + 1) товаров.
        expected_count = str(index + 1)
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), expected_count))
        
        print(f"✅ Товар {index + 1} добавлен в корзину. Всего в корзине: {expected_count}")

    # --- ПЕРЕХОД К ОФОРМЛЕНИЮ ---
    
    # Шаг 4: Переходим в корзину
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()
    
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))
    
    # Шаг 5: Checkout
    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()
    
    # Шаг 6: Заполнение формы
    wait.until(EC.element_to_be_clickable((By.ID, "first-name"))).send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    
    # Шаг 7: Нажимаем кнопку Continue
    continue_btn = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    continue_btn.click()
    
    # ПРОВЕРКА ИТОГОВОЙ СУММЫ 
    
    # 1. Ищем элемент с ФИНАЛЬНОЙ суммой (Total)
    total_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text
    
   # 2. Добавляем сбор
    import re
    match = re.search(r"\d+\.\d{2}", total_text)
    
    if not match:
        raise AssertionError(f"Price Total: {total_text}")
        
    total_value = match.group()
    
    print(f"💵 Извлеченная сумма: {total_value}")
    
    # 3. Сравниваем
    expected_total = "58.29"
    
    assert total_value == expected_total, f"Ошибка! Ожидалось ${expected_total}, но получено ${total_value}"
    
    print("✅ Тест пройден успешно! Итоговая сумма верна.")