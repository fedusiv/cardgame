import json

from communication.communication_types import MessageType


class CommunicationParser:

    # Description of fields
    login: str
    password: str

    def __init__(self, message):
        self.msg = message
        if not self.verify_msg():
            return None
        self.msg_body = self.msg["body"]
        self.msg_type = MessageType((self.msg["type"]))
        self.parse_client_message()

    def verify_msg(self):
        self.msg = json.loads(self.msg)
        if self.msg is not None:
            return True
        return False

    # Empty function, because need just to know message type
    def client_data_request(self):
        pass

    # Empty function, because need just to know message type
    def search_game_request(self):
        pass

    # For initialization client data
    # On login request it should store credentials, for further parsing and validating
    def init_client_data(self):
        self.login = self.msg_body["login"]
        self.password = self.msg_body["password"]

    # Call this function when you are sure, that message is correct
    def parse_client_message(self):
        switcher = {
            MessageType.LOGIN: self.init_client_data,
            MessageType.CLIENT_DATA: self.client_data_request,
            MessageType.SEARCH_GAME: self.search_game_request
        }
        function = switcher.get(self.msg_type)
        # Call parsing method
        function()
