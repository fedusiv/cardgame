class ClientData:
    def __init__(self, uuid: str):
        # Init with empty login name, it represents, that info from db is not received
        self.login_name = ""
        self.uuid = uuid
        self.card_dict = {}
        self.card_decks = []    # One deck looks like card_dict
