from data.values_map import VALUE_NAME_MAP


class Card:
    """
    Class object that represent the card in the deck
    """
    def __init__(self, category, value) -> None:
        self.value = value
        self.name = VALUE_NAME_MAP[value]
        self.category = category

    def get_card_info(self):
        """
        Method to retrieve current card info
        """        
        return {'name': self.name,
                'value': self.value,
                'category': self.category}
    

