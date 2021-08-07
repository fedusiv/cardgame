import json

from communication.communication_types import MessageType


class CommunicationPrepare:
    @staticmethod
    def formulate_message(body, msg_type):
        msg = {"type": msg_type,
               "body": body}
        msg_json = json.dumps(msg)
        return msg_json

    @staticmethod
    def client_data_msg(login: str, cards: list):
        body = {
            "login": login,
            "cards": cards
        }
        msg_json = CommunicationPrepare.formulate_message(body, MessageType.CLIENT_DATA.value)
        return msg_json

    @staticmethod
    def create_login_result_msg(result, uuid: str, msg=""):
        body = {
            "result": result,
            "message": msg,
            "uuid": uuid,
        }
        msg_json = CommunicationPrepare.formulate_message(body, MessageType.LOGIN.value)
        return msg_json

    @staticmethod
    def create_search_game_ack(result: bool):
        body = {
            "result" : result
        }
        msg_json = CommunicationPrepare.formulate_message(body, MessageType.SEARCH_GAME.value)
        return msg_json

    @staticmethod
    def game_started_notify():
        body = {}
        msg_json = CommunicationPrepare.formulate_message(body, MessageType.GAME_STARTED.value)
        return msg_json
