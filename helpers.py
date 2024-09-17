import requests
import random
import string

from constants import *


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_user_data():
    # Генерируем email, пароль и имя пользователя
    email = generate_random_string(5) + '@' + generate_random_string(5) + '.' + generate_random_string(2)
    password = generate_random_string(6)
    name = generate_random_string(6)

    # Собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return payload


# метод регистрации нового пользователя возвращает данные о пользователе в виде словаря
# если регистрация не удалась, возвращает None
def register_new_user_and_return_data():
    payload = generate_random_user_data()

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post(BASE_URL + REGISTER_URL, data=payload)

    if response.status_code == 200 and response.json()['success'] is True:
        # если регистрация прошла успешно
        payload["accessToken"] = response.json()['accessToken']
        payload["refreshToken"] = response.json()['refreshToken']
        return payload
    else:
        return None


def get_random_ingredients():
    response = requests.get(BASE_URL + INGREDIENTS_DATA_URL)
    data = response.json()["data"]

    # Фильтрация ингредиентов по типу
    mains = [item['_id'] for item in data if item['type'] == 'main']
    buns = [item['_id'] for item in data if item['type'] == 'bun']
    sauces = [item['_id'] for item in data if item['type'] == 'sauce']

    # Выбор случайных ингредиентов
    random_main = random.choice(mains) if mains else None
    random_bun = random.choice(buns) if buns else None
    random_sauce = random.choice(sauces) if sauces else None

    return [random_bun, random_main, random_sauce]
