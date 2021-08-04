from queue import Queue

from tornado import gen

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
        self._thread_msg_queue: Queue = Queue()

    async def logic_loop(self):
        while True:
            while self._thread_msg_queue.empty() is False:
               msg = self._thread_msg_queue.get()
            yield gen.sleep(config.LOGIC_SLEEP_TIME)
