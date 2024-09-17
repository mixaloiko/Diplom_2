import allure
import requests

from conftest import *
from constants import *


class TestOrderCreation:
    @allure.title('Создание заказа с ингредиентами неавторизованным пользователем')
    def test_order_creation_unauthorized_correct_ingredients(self, random_ingredients):
        payload = {
            "ingredients": random_ingredients
        }
        response = requests.post(BASE_URL + CREATE_ORDER_URL, data=payload)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Создание заказа без ингредиентов неавторизованным пользователем')
    def test_order_creation_unauthorized_no_ingredients(self):
        response = requests.post(BASE_URL + CREATE_ORDER_URL)
        assert response.status_code == 400 and response.json()['success'] is False and response.json()['message'] == ERROR_MESSAGE_ORDER_NO_INGREDIENTS

    @allure.title('Создание заказа с неверным хешем ингредиентов неавторизованным пользователем')
    def test_order_creation_unauthorized_incorrect_ingredients(self):
        payload = {
            "ingredients": ['000000', '111111']
        }
        response = requests.post(BASE_URL + CREATE_ORDER_URL, data=payload)
        assert response.status_code == 500

    @allure.title('Создание заказа авторизованным пользователем с ингредиентами')
    def test_order_creation_authorized_correct_ingredients(self, random_ingredients, registered_user_data):
        payload = {
            "ingredients": random_ingredients
        }
        headers = {
            'Authorization': registered_user_data['accessToken']
        }
        response = requests.post(BASE_URL + CREATE_ORDER_URL, data=payload, headers=headers)
        assert response.status_code == 200 and response.json()['success'] is True
