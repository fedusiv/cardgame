import json

class DataBase:
    # Singleton part
    _instance = None

    @staticmethod
    def instance():
        if DataBase._instance is None:
            DataBase()
        return DataBase._instance

    def __init__(self):
        DataBase._instance = self
        with open("database/table_login.json") as fake_table:
            self.table_login_json = json.load(fake_table)
        with open("database/table_clientdata.json") as fake_table:
            self.table_client_data_json = json.load(fake_table)

    # Operational part

    # Login request, return uuid of client or None if there is no such login or password mismatch
    def login_request(self, login, password):
        data = self.table_login_json
        if data[login] is None:
            return None
        elif data[login]["password"] != password:
            return None
        else:
            return data[login]["uuid"]

    def get_client_cards(self, uuid):
        cards = {}
        data = self.table_client_data_json
        if data[uuid] is not None:
            cards = data[uuid]["cards"]
        return cards

