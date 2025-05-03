class TestData:
    CORRECT_LOGIN = "PingPong"
    CORRECT_PASSWORD = "1234"
    CORRECT_NAME = "Miylz"

    ORDER_DATA = {
        "first_name": "Naruto",
        "last_name": "Uchiha",
        "address1": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
    }

    MESSAGE_CONFLICT = "Этот логин уже используется. Попробуйте другой."
    MESSAGE_BAD_REQUEST_CREAT = "Недостаточно данных для создания учетной записи"
    MESSAGE_NOT_FOUND = "Учетная запись не найдена"
    MESSAGE_BAD_REQUEST_LOGIN = "Недостаточно данных для входа"