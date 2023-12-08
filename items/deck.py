from random import choice, randrange

from data.values_map import *
from items.card import Card


class Deck:
    """
    Class object that represent the deck
    """
    def __init__(self) -> None:
        self.deck = {}
        self.top_position = 52
    
    def create(self):
        """
        Method to create a deck
        """
        self.deck = {}
        position = 1
        for category in CATEGORY_LIST:
            for number in VALUE_NAME_MAP:
                card = Card(category, number)
                self.deck[position] = card
                position += 1
        return self.deck
    
    def shuffle(self):
        """
        Method to shuffle the deck
        """
        tracker = []
        updated_deck = {}

        for position in self.deck:
            if tracker:
                new_position = choice([i for i in range(1, self.top_position+1) if i not in tracker])
            
            else:
                new_position = randrange(1,52)
                        
            updated_deck[new_position] = self.deck[position]
            tracker.append(new_position)
        
        self.deck = dict(sorted(updated_deck.items()))
        return self.deck
    
    def deal_one_card(self):
        """
        Method to deal one card from the top, the highest position number in the deck is the top card
        """
        top_card = None
        if self.top_position > 0 and self.deck:
            top_card = self.deck[self.top_position]
            del self.deck[self.top_position]
            self.top_position -= 1            
        return top_card
