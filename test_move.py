from unittest import TestCase

from A3.movement import move


class TestMove(TestCase):
    def test_move_n(self):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 2, "Y-Pos": 2}
        expected_output = {"Name": "Donna Noble", "HP": 10, "X-Pos": 2, "Y-Pos": 1}
        self.assertEqual(move(player, "N"), expected_output)

    def test_move_s(self):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 2, "Y-Pos": 2}
        expected_output = {"Name": "Donna Noble", "HP": 10, "X-Pos": 2, "Y-Pos": 3}
        self.assertEqual(move(player, "S"), expected_output)

    def test_move_w(self):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 2, "Y-Pos": 2}
        expected_output = {"Name": "Donna Noble", "HP": 10, "X-Pos": 1, "Y-Pos": 2}
        self.assertEqual(move(player, "W"), expected_output)

    def test_move_e(self):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 2, "Y-Pos": 2}
        expected_output = {"Name": "Donna Noble", "HP": 10, "X-Pos": 3, "Y-Pos": 2}
        self.assertEqual(move(player, "E"), expected_output)

    def test_move_transmat(self):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 2, "Y-Pos": 2}
        expected_output = {"Name": "Donna Noble", "HP": 10, "X-Pos": 3, "Y-Pos": 0}
        self.assertEqual(move(player, "T"), expected_output)