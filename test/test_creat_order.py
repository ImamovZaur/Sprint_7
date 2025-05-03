import requests
import json
import allure
import pytest
from urls import Urls
from data import TestData

class TestCreateOrder:
    @allure.description('Возможности создания самоката с выбором цвета')
    @pytest.mark.parametrize('chosen_color', ['BLACK', 'GREY', ['BLACK', 'GREY'], ''])
    def test_create_order_with_black_and_grey_color(self, chosen_color):
        TestData.ORDER_DATA['color'] = [chosen_color]
        order_data_json = json.dumps(TestData.ORDER_DATA)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Urls.CREATE_ORDER_URL, data=order_data_json, headers=headers)
        assert (response.status_code == 201 and 'track' in response.text)