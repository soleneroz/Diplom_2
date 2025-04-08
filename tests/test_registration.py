import requests
import pytest
import allure
from data import *
from url import *


class TestRegistration:
    @allure.title('Успешная регистрация')
    def test_registration_account(self):
        payload = {
            'email': get_random_email(), 'password': get_random_password(), 'name': get_random_username()
        }
        response = requests.post(Url.register_user, data=payload)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        access_token = deserials['accessToken']
        requests.delete(Url.delete_user, headers={'Authorization': access_token})


    @allure.title('Регистрация с уже используемой почтой')
    def test_registration_witn_email_already_have(self):
        payload = {
            'email': UserData.email, 'password': get_random_password(), 'name': get_random_username()
        }
        response = requests.post(Url.register_user, data=payload)
        assert response.status_code == 403 and response.json() == {'success': False, 'message': 'User already exists'}


    @allure.title('Регистрация без заполнения обязательных полей')
    @pytest.mark.parametrize('creds', UserData.empty_fields_creds)
    def test_registration_with_empty_fields(self, creds):
        response = requests.post(Url.register_user, data=creds)
        assert (response.status_code == 403 and response.json() == {'success': False, 'message': 'Email, password and name are required fields'})
