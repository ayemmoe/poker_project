class Player:
    """
    class object that represents Player
    """
    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_card_counts(self):
        """
        Method to retrieve current card counts the player hold
        """
        return len(self.cards)
