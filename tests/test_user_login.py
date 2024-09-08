import allure
import requests

from conftest import *
from constants import *


class TestUserLogin:
    @allure.title('Проверка логина под существующим пользователем')
    def test_user_login(self, registered_user_data):
        payload = {
            "email": registered_user_data['email'],
            "password": registered_user_data['password']
        }
        response = requests.post(BASE_URL + LOGIN_URL, data=payload)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка логина с некорректным имеелом и паролем')
    def test_user_login_with_incorrect_email_and_password(self, random_user_data):
        payload = {
            "email": random_user_data['email'],
            "password": random_user_data['password']
        }
        response = requests.post(BASE_URL + LOGIN_URL, data=payload)
        assert response.status_code == 401 and response.json()['success'] is False and response.json()['message'] == INCORRECT_EMAIL_AND_PASSWORD


