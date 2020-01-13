from unittest import TestCase
from unittest.mock import patch

from A3.fight import hit_or_miss


class TestHit_or_miss(TestCase):
    @patch("A3.fight.roll_die", side_effect=[5, 1])
    def test_hit_or_miss_yes(self, mock_roll):
        attacker = {"Name": "Dalek"}
        self.assertTrue(hit_or_miss(attacker))

    @patch("A3.fight.roll_die", side_effect=[1, 5])
    def test_hit_or_miss_no(self, mock_roll):
        attacker = {"Name": "Dalek"}
        self.assertFalse(hit_or_miss(attacker))
