import allure
import requests

from conftest import *
from constants import *


class TestUserOrders:

    @allure.title('Проверка получения списка заказов авторизированного пользователя')
    def test_user_orders_authorized(self, registered_user_data, random_ingredients):
        payload = {
            "ingredients": random_ingredients
        }
        headers = {
            'Authorization': registered_user_data['accessToken']
        }
        response = requests.post(BASE_URL + CREATE_ORDER_URL, data=payload, headers=headers)
        response = requests.get(BASE_URL + CREATE_ORDER_URL, headers=headers)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка получения заказов неавторизированного пользователя')
    def test_user_orders_unauthorized(self):
        response = requests.get(BASE_URL + CREATE_ORDER_URL)
        assert response.status_code == 401 and response.json()['success'] is False and response.json()['message'] == ERROR_MESSAGE_UNAUTHORIZED
