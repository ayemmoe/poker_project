import unittest
from items.card import Card


class TestCard(unittest.TestCase):
    def test_card_ace(self):
        """
        Test a heart ace card is created successfully
        """
        heart_ace = Card('heart', 1)
        self.assertEqual(heart_ace.category, 'heart', 'Failed to validate category ')
        self.assertEqual(heart_ace.name, 'ace', 'Failed to validate name')
        self.assertEqual(heart_ace.value, 1, 'Failed to validate value')

    def test_card_number(self):
        """
        Test a heart three card is created successfully
        """
        heart_three = Card('heart', 3)
        self.assertEqual(heart_three.category, 'heart', 'Failed to validate category ')
        self.assertEqual(heart_three.name, 'three', 'Failed to validate name')
        self.assertEqual(heart_three.value, 3, 'Failed to validate value')

    def test_card_jack(self):
        """
        Test a spade jack card is created successfully
        """
        spade_jack = Card('spade', 11)
        self.assertEqual(spade_jack.category, 'spade', 'Failed to validate category ')
        self.assertEqual(spade_jack.name, 'jack', 'Failed to validate name')
        self.assertEqual(spade_jack.value, 11, 'Failed to validate value')

    def test_card_queen(self):
        """
        Test a club queen card is created successfully
        """
        club_queen = Card('club', 12)
        self.assertEqual(club_queen.category, 'club', 'Failed to validate category ')
        self.assertEqual(club_queen.name, 'queen', 'Failed to validate name')
        self.assertEqual(club_queen.value, 12, 'Failed to validate value')

    def test_card_king(self):
        """
        Test a diamond king card is created successfully
        """
        diamond_king = Card('diamond', 13)
        self.assertEqual(diamond_king.category, 'diamond', 'Failed to validate category ')
        self.assertEqual(diamond_king.name, 'king', 'Failed to validate name')
        self.assertEqual(diamond_king.value, 13, 'Failed to validate value')

    def test_get_card_info(self):
        """
        Test get_card_info method
        """
        spade_king = Card('spade', 13)
        card_info = spade_king.get_card_info()
        self.assertEqual(len(card_info), 3, 'Failed to validate the length of card info')
        self.assertEqual(card_info['name'], 'king', 'Failed to validate card info name')
        self.assertEqual(card_info['value'], 13, 'Failed to validate card info value')
        self.assertEqual(card_info['category'], 'spade', 'Failed to validate card category')


if __name__ == '__main__':
    unittest.main()
