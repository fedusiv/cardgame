class CardObj:
    id: int  # unique id of the card in whole list of cards
    name: str
    cost: int

    def __init__(self, card_id: int):
        self.id = card_id
