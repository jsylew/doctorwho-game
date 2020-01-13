from unittest import TestCase
from unittest.mock import patch

from A3.fight import calc_damage


class TestCalc_damage(TestCase):
    @patch("A3.fight.roll_die", return_value=2)
    def test_calc_damage(self, mock_roll):
        self.assertEqual(calc_damage(), 2)
