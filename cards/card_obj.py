from cards.card_enums import CardObjType


class CardObj:
    id: int  # unique id of the card in whole list of cards
    name: str
    price: int
    card_type: CardObjType

    # To create card we will fill it with default information, that all cards have
    def __init__(self, card_id: int, card_name: str,
                 card_price: int, card_type: CardObjType):
        self.id = card_id
        self.name = card_name
        self.price = card_price
        self.card_type = card_type

