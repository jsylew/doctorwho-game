from unittest import TestCase
from unittest.mock import patch

from A3.helpers import roll_die


class TestRoll_die(TestCase):
    @patch("random.randint", return_value=2)
    def test_roll_die_1d6(self, mock_roll):
        self.assertEqual(roll_die(1, 6), 2)

    @patch("random.randint", side_effect=[2, 7])
    def test_roll_die_2d8(self, mock_roll):
        self.assertEqual(roll_die(2, 8), 9)
