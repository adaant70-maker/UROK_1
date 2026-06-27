from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:

        # Cookie для пользователя 1 

        user1_cookies = [
            {'name': "SESSION", 
            'value': 'NjUxNDBmZTEtMzM5ZS00MzZhLWJiNTQtN2Q4YTdkMGUxNjNl', 
            'domain': 'gitflic.ru'}
        ]

        # Cookie для пользователя 2 

        user2_cookies = [
            {'name': "SESSION", 
            'value': 'NDQ2ODc1MDktNjZjYy00NzJmLTgwYTItYzQ1YzJjNmQ3MTI0',
            'domain': 'gitflic.ru'},
        ]