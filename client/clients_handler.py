from client.client_operation import ClientOperation

class ClientsHandler:
    # Singleton part
    _instance = None

    @staticmethod
    def instance():
        if ClientsHandler._instance is None:
            ClientsHandler()
        return ClientsHandler._instance

    def __init__(self):
        ClientsHandler._instance = self
        self.clients_dict = {}

    def append_client(self, client: ClientOperation):
        self.clients_dict = {client.client_data.uuid: client}

    def remove_client(self, client: ClientOperation):
        if client.client_data is None:
            return
        self.clients_dict.pop(client.client_data.uuid)

    def get_client_handler(self, client_uuid: str):
        return self.clients_dict.get(client_uuid)
