import requests
import json
import allure
import pytest
from urls import Urls

class TestGetOrderList:
    @allure.title('Проверка получения списка заказов')
    def test_get_order_list(self):
        response = requests.get(Urls.GET_ORDERS_LIST_URL)
        orders = response.json().get('orders')
        assert response.status_code == 200 and 'orders' in response.text
        assert orders is not None