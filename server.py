import tornado.web
import tornado.websocket
import tornado.ioloop
import tornado.options

from client.client_handler import ClientHandler
import config
from database.database import DataBase
from logic.server_logic import ServerLogic


class Server(tornado.web.Application):
    def __init__(self, io_loop):
        handlers = [(r"/", ClientHandler)]
        settings = dict(debug=True)
        tornado.web.Application.__init__(self, handlers, **settings)
        self.io_loop = io_loop
        # Init database
        self.database = DataBase.instance()
        # Init main logic loop
        self.server_logic = ServerLogic.instance()
        self.server_logic.send_io_loop(self.io_loop)
        self.io_loop.spawn_callback(self.server_logic.logic_loop)


def server_start() -> None:
    io_loop_instance = tornado.ioloop.IOLoop.current()
    server = Server(io_loop_instance)
    server.listen(config.PORT)

    # After this line nothing will act, because it starts infinite priority loop
    print("Server has started")
    io_loop_instance.start()
