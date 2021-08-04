from enum import Enum, unique


@unique
class MessageType(Enum):
    NONE = 0
    LOGIN = 1
    CLIENT_DATA = 2
    SEARCH_GAME = 3


