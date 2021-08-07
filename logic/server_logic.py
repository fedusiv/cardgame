from tornado import gen
import tornado.ioloop

from communication.communication_parser import CommunicationParser
from communication.communication_types import MessageType
from logic.server_logic_queue import ServerLogicQueue
from game.game_session import GameSession
import config


class ServerLogic:
    # Singleton part
    _instance = None

    @staticmethod
    def instance():
        if ServerLogic._instance is None:
            ServerLogic()
        return ServerLogic._instance

    def __init__(self):
        ServerLogic._instance = self
        self.logic_queue = ServerLogicQueue.instance()
        # List of client's uuid, which searches game
        self.search_list = []
        # list of game sessions
        self.game_sessions = []
        # create empty loop
        self.io_loop = None

    def send_io_loop(self, io_loop: tornado.ioloop.IOLoop):
        self.io_loop = io_loop

    def add_to_game_search(self, msg: CommunicationParser):
        if msg.uuid in self.search_list:
            # Client is already there, no need to do anything
            return
        self.search_list.append(msg.uuid)
        while self.search_list.count() > 1:
            # Create game session
            player1 = self.search_list.pop()
            player2 = self.search_list.pop()
            # Create game session
            game_session = GameSession(player1, player2)
            self.game_sessions.append(game_session)
            # Start session
            self.io_loop.spawn_callback(game_session.main_loop)

    async def logic_loop(self):
        while True:
            while self.logic_queue.empty() is False:
                msg: CommunicationParser = self.logic_queue.get_element()
                switcher = {
                    MessageType.SEARCH_GAME : self.logic_queue
                }
                function = switcher.get(msg.msg_type)
                function(msg)
            yield gen.sleep(config.LOGIC_SLEEP_TIME)
