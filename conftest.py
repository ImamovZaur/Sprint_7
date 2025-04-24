import pytest
import requests
from urls import *
from helpers import *


@pytest.fixture
def delete_courier():
    courier = register_new_courier_with_static_data()
    courier_login = requests.post(Urls.LOGIN_COURIER_URL, data={'login': courier['login'], 'password': courier['password']})
    courier_id = courier_login.json().get('id')
    courier_delete = requests.delete(f'{Urls.MAIN_URL}/api/v1/courier/{courier_id}')
    return {'status': courier_delete.status_code,
            'text': courier_delete.json()}