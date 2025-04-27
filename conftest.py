import pytest
import requests
from urls import *
from helpers import *


@pytest.fixture
def create_delete_courier():
    courier = register_new_courier_with_static_data()
    response = requests.post(Urls.CREATE_COURIER_URL, data=courier)
    yield response
    courier_login = requests.post(Urls.LOGIN_COURIER_URL, data={'login': courier['login'], 'password': courier['password']})
    courier_id = courier_login.json().get('id')
    courier_delete = requests.delete(f'{Urls.MAIN_URL}/api/v1/courier/{courier_id}')

@pytest.fixture()
def delete_courier():
    def _delete_courier(courier):
        courier_login = requests.post(Urls.LOGIN_COURIER_URL, data={'login': courier['login'], 'password': courier['password']})
        courier_id = courier_login.json().get('id')
        courier_delete = requests.delete(f'{Urls.MAIN_URL}/api/v1/courier/{courier_id}')
        return courier_delete
    return _delete_courier