import allure
import requests

from conftest import *
from constants import *


class TestUserCreation:
    @allure.title('Проверка создания пользователя')
    def test_user_creation(self, random_user_data):
        response = requests.post(BASE_URL + REGISTER_URL, data=random_user_data)

        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка, что нельзя создать двух одинаковых пользователей')
    def test_duplicate_user_creation(self, random_user_data):
        response = requests.post(BASE_URL + REGISTER_URL, data=random_user_data)
        response = requests.post(BASE_URL + REGISTER_URL, data=random_user_data)

        assert response.status_code == 403 and response.json()['success'] is False and response.json()['message'] == DUPLICATE_USER_REGISTER_ERROR_MESSAGE

    @allure.title('Проверка, что нельзя создать пользователей с пустым полем')
    def test_empty_field_user_creation(self, random_user_data):
        random_user_data ['email'] = ''
        response = requests.post(BASE_URL + REGISTER_URL, data=random_user_data)
        response = requests.post(BASE_URL + REGISTER_URL, data=random_user_data)

        assert response.status_code == 403 and response.json()['success'] is False and response.json()['message'] == EMPTY_FIELD_USER_REGISTER_ERROR_MESSAGE