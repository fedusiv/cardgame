import tornado
import tornado.websocket

from client.client_data import ClientData
from communication.communication_parser import CommunicationParser
from communication.communication_prepare import CommunicationPrepare
from communication.communication_types import MessageType
from logic.server_logic_queue import ServerLogicQueue
from database.database import DataBase


class ClientOperation:

    client_data: ClientData

    def __init__(self, wsh: tornado.websocket.WebSocketHandler):
        self.ws: tornado.websocket.WebSocketHandler = wsh
        self.logic_queue = ServerLogicQueue.instance()
        self.database = DataBase.instance()
        self.is_logged = False

    def login_request(self, message: CommunicationParser):
        uuid = self.database.login_request(message.login, message.password)
        if uuid is not None:
            print("Logged client: " + message.login)
            self.client_data = ClientData(uuid)
            self.client_data.login_name = message.login
            self.client_data.card_dict = self.database.get_client_cards(uuid)
            self.is_logged = True
        else:
            uuid = ""
        msg = CommunicationPrepare.create_login_result_msg(self.is_logged, uuid)
        self.ws.write_message(msg)

    def game_started_notify(self):
        msg = CommunicationPrepare.game_started_notify()
        self.ws.write_message(msg)

    def search_game_request(self, msg):
        # Put element
        self.logic_queue.put_element(msg)
        # Inform client, that he is on search queue
        msg = CommunicationPrepare.create_search_game_ack(True)
        self.ws.write_message(msg)

    # Send client data by request
    def client_data_request(self, msg):
        msg = CommunicationPrepare.client_data_msg(self.client_data.login_name, self.client_data.card_dict)
        self.ws.write_message(msg)

    def react_on_message(self, msg: CommunicationParser):
        switcher = {
            MessageType.CLIENT_DATA: self.client_data_request,
            MessageType.SEARCH_GAME: self.search_game_request
        }
        function = switcher.get(msg.msg_type, self.empty_error_react)
        function(msg)

    def read_message(self, message: CommunicationParser):
        if self.is_logged:
            self.react_on_message(message)
        else:
            if message.msg_type == MessageType.LOGIN:
                self.login_request(message)

    def empty_error_react(self):
        pass
