import pytest
import allure
import requests
from data import *
from url import *


@pytest.fixture
@allure.title('Создание рандомного пользователя и его удаление')
def create_user_and_delete():
    payload_cred = {
        'email': get_random_email(), 'password': get_random_password(), 'name': get_random_username()
    }
    response = requests.post(Url.register_user, data=payload_cred)
    response_body = response.json()
    yield payload_cred, response_body
    access_token = response_body['accessToken']
    requests.delete(Url.delete_user, headers={'Authorization': access_token})


@pytest.fixture
@allure.title('Создание рандомного пользователя и заказа, затем удаление пользователя')
def create_user_and_order(create_user_and_delete):
    access_token = create_user_and_delete[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [IngredientData.burger]}
    response_body = requests.post(Url.get_order, data=payload, headers=headers)
    yield access_token, response_body
    requests.delete(Url.delete_user, headers={'Authorization': access_token})