class ClientData:
    def __init__(self, uuid: str):
        # Init with empty login name, it represents, that info from db is not received
        self.login_name = "test_login"
        self.uuid = uuid
        self.card_list = ["test-1", "test-2"]
