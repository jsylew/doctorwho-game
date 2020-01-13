from unittest import TestCase

from A3.movement import check_transmat


class TestCheck_transmat(TestCase):
    def test_check_transmat_yes(self):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 0, "Y-Pos": 0}
        board = {(0, 0): {"Transmat": True}}
        self.assertTrue(check_transmat(player, board))

    def test_check_transmat_no(self):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 0, "Y-Pos": 0}
        board = {(0, 0): {"Transmat": False}}
        self.assertFalse(check_transmat(player, board))