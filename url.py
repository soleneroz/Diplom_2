class Url:
    base_url = 'https://stellarburgers.nomoreparties.site'
    headers = {'Content-Type': 'application/json'}
    register_user = f'{base_url}/api/auth/register'
    auth_user = f'{base_url}/api/auth/login'
    update_user = f'{base_url}/api/auth/user'
    delete_user = f'{base_url}/api/auth/user'
    get_order = f'{base_url}/api/orders'
    get_user_orders = f'{base_url}/api/orders'
