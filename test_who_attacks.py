from unittest import TestCase
from unittest.mock import patch

from A3.fight import who_attacks


class TestWho_attacks(TestCase):
    @patch("A3.fight.roll_die", side_effect=[6, 1])
    def test_who_attacks_player_first(self, mock_roll):
        player = {"Name": "Donna Noble"}
        creature = {"Name": "Dalek"}
        attacker, defender = who_attacks(player, creature)
        self.assertDictEqual(attacker, player)

    @patch("A3.fight.roll_die", side_effect=[1, 6])
    def test_who_attacks_creature_first(self, mock_roll):
        player = {"Name": "Donna Noble"}
        creature = {"Name": "Dalek"}
        attacker, defender = who_attacks(player, creature)
        self.assertDictEqual(attacker, creature)
