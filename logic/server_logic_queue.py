from queue import Queue


class ServerLogicQueue:
    # Singleton part
    _instance = None

    @staticmethod
    def instance():
        if ServerLogicQueue._instance is None:
            ServerLogicQueue()
        return ServerLogicQueue._instance

    def __init__(self):
        ServerLogicQueue._instance = self
        self._queue: Queue = Queue()

    # Return true if queue is not empty
    @property
    def non_empty(self):
        return not self._queue.empty()

    # Get next element in queue
    def get_element(self):
        return self._queue.get()

    # Put element inside
    def put_element(self, element):
        self._queue.put(element)
