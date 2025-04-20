import requests
import allure
import pytest
from data import TestData
from helpers import *
from urls import Urls

class TestCreateCourier:
    @allure.title('Тест создания курьера')
    @allure.description('Проверка создания курьера')
    def test_create_courier_account_created(self):
        courier = register_new_courier_and_return_login_password()
        response = requests.post(Urls.CREATE_COURIER_URL, data=courier)
        assert response.status_code == 201 and response.json() == {'ok': True}

    @allure.title('Создание существующего курьера')
    def test_create_duplicate_courier(self):
        courier_payload = register_new_courier_with_static_data()
        requests.post(Urls.CREATE_COURIER_URL, data=courier_payload)
        second_response = requests.post(Urls.CREATE_COURIER_URL, data=courier_payload)
        assert (second_response.status_code == 409 and
                second_response.json().get('message') == TestData.MESSAGE_CONFLICT)

    @allure.title('Создание курьера с одним незаполненным полем')
    @pytest.mark.parametrize('fields', [{'login': '', 'password': generate_password(), 'firstName': generate_first_name()},
                             {'login': generate_login(), 'password': '', 'firstName': generate_first_name()}
                             ])
    def test_create_courier_with_empty_fields(self, fields):
        response = requests.post(Urls.CREATE_COURIER_URL, data=fields)
        assert (response.status_code == 400 and
                response.json().get('message') == TestData.MESSAGE_BAD_REQUEST_CREAT)