import unittest

from items.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_one = Player('Alex')
        self.player_two = Player('George')
        self.player_three = Player('Macy')

    def test_player(self):
        """
        Test player object creation
        """
        self.assertEqual(self.player_one.name, 'Alex', 'Failed to validate player_one name')
        self.assertEqual(self.player_two.name, 'George', 'Failed to validate player_one name')
        self.assertEqual(self.player_three.name, 'Macy', 'Failed to validate player_one name')
        self.assertEqual(self.player_one.get_card_counts(), 0, 'Failed to validate initial value of player_one cards')
        self.assertEqual(self.player_two.get_card_counts(), 0, 'Failed to validate initial value of player_two cards')
        self.assertEqual(self.player_three.get_card_counts(), 0, 'Failed to validate initial value '
                                                                 'of player_three cards')
