from conftest import *


class TestAuthentication:
    @allure.title('Успешная авторизация с валидными данными')
    def test_auth(self, create_user_and_delete):
        payload = create_user_and_delete[0]
        response = requests.post(Url.auth_user, data=payload)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True

    @allure.title('Авторизация с невалидной почтой')
    def test_auth_invalid_email(self):
        payload = {
            'email': get_random_email(),
            'password': UserData.password,
        }
        response = requests.post(Url.auth_user, data=payload)
        assert response.status_code == 401 and response.json() == {"success": False, "message": "email or password are incorrect"}

    @allure.title('Авторизация с неверным паролем')
    def test_auth_wrong_password(self):
        payload = {
            'email': UserData.email,
            'password': get_random_password(),
        }
        response = requests.post(Url.auth_user, data=payload)
        assert response.status_code == 401 and response.json() == {"success": False, "message": "email or password are incorrect"}
