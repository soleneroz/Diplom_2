from conftest import *


class TestUpdateUser:

    updated_user = {
        'email': get_random_email(),
        'password': get_random_password(),
        'name': get_random_username()
    }

    @allure.title('Изменение данных авторизованного пользователя')
    def test_update_authorized_user(self, create_user_and_delete):
        response = requests.patch(Url.update_user, headers={'Authorization': create_user_and_delete[1]['accessToken']}, data=TestUpdateUser.updated_user)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert deserials['user']['name'] == TestUpdateUser.updated_user['name']
        assert deserials['user']['email'] == TestUpdateUser.updated_user['email']


    @allure.title('Изменение данных неавторизованного пользователя')
    def test_update_unauthorized_user(self):
        response = requests.patch(Url.update_user, headers=Url.headers, data=TestUpdateUser.updated_user)
        assert response.status_code == 400
