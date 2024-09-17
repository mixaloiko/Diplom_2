import allure
import requests

from conftest import *
from constants import *


class TestEditUserData:
    @allure.title('Изменение данных пользователя с авторизацией')
    def test_edit_user_unauthorized(self, random_user_data):
        response = requests.patch(BASE_URL + EDIT_USER_DATA_URL, data=random_user_data)

        assert response.status_code == 401 and response.json()['success'] is False and response.json()[
            'message'] == ERROR_MESSAGE_UNAUTHORIZED

    @allure.title('Изменение данных пользователя с авторизацией')
    def test_edit_user_authorized(self, registered_user_data, random_user_data):
        headers = {
            'Authorization': registered_user_data['accessToken']
        }

        response = requests.patch(BASE_URL + EDIT_USER_DATA_URL, data=random_user_data, headers=headers)

        assert response.status_code == 200 and response.json()['success'] is True

