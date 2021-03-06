import tornado.web
import tornado.websocket
import tornado.ioloop
import tornado.options

from client.client_data import ClientData
from client.client_operation import ClientOperation
from client.clients_handler import ClientsHandler
from communication.communication_parser import CommunicationParser
from communication.communication_types import MessageType
from communication.communication_prepare import CommunicationPrepare
from database.database import DataBase


class ClientHandler(tornado.websocket.WebSocketHandler):

    # Class fields
    operation: ClientOperation  # Client operation module
    handler: ClientsHandler  # Where all clients connected right now are stored
    in_handler = False

    def open(self):
        print("A client connected to server. ", self.request.remote_ip)
        self.operation = ClientOperation(self)

    def on_close(self):
        if self.in_handler:
            print("A client disconnected", self.operation.client_data.login_name)
            self.handler.remove_client(self.operation)
        else:
            print("Unlogged noname disconnected")

    def on_message(self, message):
        result: CommunicationParser = CommunicationParser(message)
        if result is None:
            # Wrong message do nothing
            return
        self.operation.read_message(result)
        # Create handler list
        if not self.in_handler:
            if self.operation.is_logged:
                self.handler = ClientsHandler.instance()
                self.handler.append_client(self.operation)
                self.in_handler = True


