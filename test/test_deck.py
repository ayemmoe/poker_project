import unittest

from items.deck import Deck
from items.player import Player


class TestDeck(unittest.TestCase):
    def setUp(self):
        """
        Setup deck object
        """
        self.deck_obj = Deck()
        self.deck_obj.create()

    def test_deck_create(self):
        """
        Test create method
        """
        deck_categories = {}
        expected_categories = ['heart', 'spade', 'club', 'diamond']
        expected_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        for card in self.deck_obj.deck:
            if not self.deck_obj.deck[card].category in deck_categories:
                deck_categories[self.deck_obj.deck[card].category] = [self.deck_obj.deck[card].value]
            else:
                deck_categories[self.deck_obj.deck[card].category].append(self.deck_obj.deck[card].value)

        self.assertEqual(len(self.deck_obj.deck), 52, 'Failed to validate created deck has 52 cards')

        for category in deck_categories:
            self.assertIn(category, expected_categories, f'Failed to validate {category} is part of the expected '
                                                         f'{expected_categories}')
            self.assertEqual(len(deck_categories[category]), 13, f'Failed to validate total card counts '
                                                                 f'for {category} is 13.')
            self.assertListEqual(deck_categories[category], expected_values, 'Failed to validate values')

    def test_deck_shuffle(self):
        """
        Test shuffle method
        """
        original_deck_dict = {}
        for position in self.deck_obj.deck:
            original_deck_dict[position] = self.deck_obj.deck[position].get_card_info()

        self.deck_obj.shuffle()
        shuffle_deck_dict = {}
        for position in self.deck_obj.deck:
            shuffle_deck_dict[position] = self.deck_obj.deck[position].get_card_info()

        self.assertEqual(len(shuffle_deck_dict), 52, 'Failed to validate the shuffled deck has 52 cards')
        self.assertNotEqual(original_deck_dict, shuffle_deck_dict, 'Failed to validate after shuffle deck is '
                                                                   'different from original deck')

    def test_deck_deal_one_card(self):
        """
        test deal_one_card method
        """
        player_one = Player('Amy')
        for number in range(1, 53):
            top_card = self.deck_obj.deck[self.deck_obj.top_position]
            top_card_info = top_card.get_card_info()
            deal = self.deck_obj.deal_one_card(player_one)
            deal_card_info = deal.get_card_info()

            self.assertDictEqual(top_card_info, deal_card_info, 'Failed to validate the top card is the same as '
                                                                'the deal card')
            self.assertEqual(len(self.deck_obj.deck), 52-number, f'Failed to validate the size of the deck is '
                                                                 f'reduced to {52-number} after the {number} deal')
            self.assertEqual(player_one.get_card_counts(), number, 'Failed to validate player one card count increased')


class TestDeckEmpty(unittest.TestCase):
    def setUp(self):
        """
        Set up an empty deck object
        """
        self.deck_obj = Deck()

    def test_deck_empty_shuffle(self):
        """
        Test shuffle method to an empty deck object
        """
        self.deck_obj.shuffle()
        self.assertEqual(len(self.deck_obj.deck), 0, 'Failed to validate the deck is empty after shuffle')

    def test_deck_empty_deal_one_card(self):
        """
        Test deal_one_card method to an empty deck object
        """
        player_two = Player('David')
        deal_card = self.deck_obj.deal_one_card(player_two)
        print(f'{player_two.name} cards', player_two.cards)
        print('david card counts', player_two.get_card_counts())
        self.assertIsNone(deal_card, 'Failed to validate deal card is None')
        self.assertEqual(player_two.get_card_counts(), 0, 'Failed to validate player 2 card count not change')


if __name__ == '__main__':
    unittest.main()
