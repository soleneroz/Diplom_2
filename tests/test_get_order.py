from conftest import *


class TestGetOrder:
    @allure.title('Создание заказа с ингридиентами авторизованным пользователем')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger])
    def test_get_order_user_authorized(self, create_user_and_delete, burger_ingredients):
        headers = {'Authorization': create_user_and_delete[1]['accessToken']}
        payload = {'ingredients': [burger_ingredients]}
        response = requests.post(Url.get_order, data=payload, headers=headers)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'name' in deserials.keys() and 'number' in deserials['order'].keys()

    @allure.title('Создание заказа без ингридиентов авторизованным пользователем')
    def test_get_order_without_ingredients_user_authorized(self, create_user_and_delete):
        headers = {'Authorization': create_user_and_delete[1]['accessToken']}
        payload = {'ingredients': []}
        response = requests.post(Url.get_order, data=payload, headers=headers)
        assert response.status_code == 400 and response.json() == {'success': False, 'message': 'Ingredient ids must be provided'}

    @allure.title('Создание заказа без ингридиентов неавторизованным пользователем')
    def test_get_order_without_ingredients_user_unauthorized(self):
        payload = {'ingredienst': []}
        response = requests.post(Url.get_order, data=payload, headers=Url.headers)
        assert response.status_code == 400 and response.json() == {'success': False, 'message': 'Ingredient ids must be provided'}

    @allure.title('Создание заказа авторизованным пользователем с невалидным хэшем')
    def test_get_order_invalid_ingredients_user_authorized(self, create_user_and_delete):
        headers = {'Authorization': create_user_and_delete[1]['accessToken']}
        payload = {'ingredients': [IngredientData.invalid_hash]}
        response = requests.post(Url.get_order, data=payload, headers=headers)
        assert response.status_code == 500


    @allure.title('Создание заказа неавторизованным пользователем с ингридиентами')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger])
    def test_create_order_unauthenticated_user_success(self, burger_ingredients):
        payload = {'ingredients': [burger_ingredients]}
        response = requests.post(Url.get_order, data=payload, headers=Url.headers)
        assert response.status_code == 400


    @allure.title('Создание заказа неавторизованным пользователем с невалидным хэшем')
    def test_get_order_invalid_ingredients_user_authorized(self):
        payload = {'ingredients': [IngredientData.invalid_hash]}
        response = requests.post(Url.get_order, data=payload, headers=Url.headers)
        assert response.status_code == 400
