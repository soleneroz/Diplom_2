from conftest import *
import requests


class TestGetUsersOrders:
    @allure.title('Получение заказов для авторизованного пользователя')
    def test_get_authorized_users_orders(self, create_user_and_order):
        headers = {'Authorization': create_user_and_order[0]}
        response = requests.get(Url.get_user_orders, headers=headers)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'orders' in deserials.keys() and 'total' in deserials.keys()

    @allure.title('Получение заказов для неавторизованного пользователя')
    def test_get_unauthorized_users_orders(self):
        response = requests.get(Url.get_user_orders, headers=Url.headers)
        assert response.status_code == 401 and response.json() == {'success': False, 'message': 'You should be authorised'}
