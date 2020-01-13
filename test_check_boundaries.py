from unittest import TestCase

from A3.movement import check_boundaries


class TestCheck_boundaries(TestCase):
    def test_check_boundaries(self):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 0, "Y-Pos": 0}
        board = {(0, 0): {"Walls": ["N", "S"]}}
        self.assertEqual(check_boundaries(player, board), ["N", "S"])
