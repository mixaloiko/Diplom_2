import pytest

from helpers import generate_random_user_data, register_new_user_and_return_data, get_random_ingredients


@pytest.fixture()
def random_user_data():
    payload = generate_random_user_data()

    return payload


@pytest.fixture()
def registered_user_data():
    user_data = register_new_user_and_return_data()

    return user_data


@pytest.fixture()
def random_ingredients():
    ingredients = get_random_ingredients()

    return ingredients
