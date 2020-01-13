from unittest import TestCase

from A3.movement import check_tardis


class TestCheck_tardis(TestCase):
    def test_check_tardis_yes(self):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 0, "Y-Pos": 0}
        board = {(0, 0): {"TARDIS": True}}
        self.assertTrue(check_tardis(player, board))

    def test_check_tardis_no(self):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 0, "Y-Pos": 0}
        board = {(0, 0): {"TARDIS": False}}
        self.assertFalse(check_tardis(player, board))
