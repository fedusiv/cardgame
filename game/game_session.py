from client.client_operation import ClientOperation


class GameSession:
    def __init__(self, player1: ClientOperation, player2: ClientOperation):
        # Inform players, that game session is created
        player1.game_started_notify()
        player2.game_started_notify()

    def main_loop(self):
        while True:
            pass
