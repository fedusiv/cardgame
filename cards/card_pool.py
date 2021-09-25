from cards.card_pool_builder import CardPoolBuilder


class CardPool:
    # Singleton part
    _instance = None

    @staticmethod
    def instance():
        if CardPool._instance is None:
            CardPool()
        return CardPool._instance

    def __init__(self):
        CardPool.__instance = self
        self.card_pool_dict = {}
        self.builder = CardPoolBuilder()
        self.parse_db()

    def parse_db(self):
        graveyard_list = self.builder.build_from_excel("cards_description/graveyard.xlsx")
        for card in graveyard_list:
            self.card_pool_dict[card.id] = card
