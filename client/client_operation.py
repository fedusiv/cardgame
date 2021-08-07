import tornado

from client.client_data import ClientData
from communication.communication_parser import CommunicationParser
from communication.communication_prepare import CommunicationPrepare
from communication.communication_types import MessageType
from logic.server_logic_queue import ServerLogicQueue


class ClientOperation:

    client_data: ClientData

    def __init__(self, ws: tornado.websocket.WebSocketHandler):
        self.ws: tornado.websocket.WebSocketHandler = ws
        self.logic_queue = ServerLogicQueue.instance()
        self.is_logged = False

    def login_request(self,message: CommunicationParser):
        print("Logged client: " + message.login)
        self.client_data = ClientData("a1")
        self.is_logged = True
        msg = CommunicationPrepare.create_login_result_msg(True, "a1")
        self.ws.write_mesage(msg)

    def game_started_notify(self):
        msg = CommunicationPrepare.game_started_notify()
        self.ws.write_mesage(msg)

    def search_game_request(self, msg):
        # Put element
        self.logic_queue.put_element(msg)
        # Inform client, that he is on search queue
        msg = CommunicationPrepare.create_search_game_ack(True)
        self.ws.write_mesage(msg)

    # Send client data by request
    def client_data_request(self):
        msg = CommunicationPrepare.client_data_msg(self.client_data.login_name, self.client_data.card_list)
        self.ws.write_mesage(msg)

    def react_on_message(self, msg: CommunicationParser):
        if msg.uuid != self.client_data.uuid:
            # Not uuid of current client
            return
        switcher = {
            MessageType.CLIENT_DATA: self.client_data,
            MessageType.SEARCH_GAME: self.search_game_request
        }
        function = switcher.get(msg.msg_type, self.empty_error_react)
        function(msg)

    def read_message(self, message: CommunicationParser):
        if self.is_logged:
            pass
        else:
            if message.msg_type == MessageType.LOGIN:
                self.login_request(message)

    def empty_error_react(self):
        pass
