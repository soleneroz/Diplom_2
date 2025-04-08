from random_data import *


class UserData:
    email = 'nikita_kopyev_17_777@yandex.ru'
    password = 'kopyev'
    username = 'Bravado'

    empty_fields_creds = [
        {
         'email': '',
         'password': get_random_password(),
         'name': get_random_username()
         },

        {
         'email': get_random_email(),
         'password': '',
         'name': get_random_username()
         },

        {
         'email': get_random_email(),
         'password': get_random_password(),
         'name': ''
         }
    ]


class IngredientData:

    burger = ['61c0c5a71d1f82001bdaaa70', '61c0c5a71d1f82001bdaaa75', '61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6d']

    invalid_hash = '61c0c5a71d1f02345123456'