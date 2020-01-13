from unittest import TestCase
from unittest.mock import patch

from A3.movement import check_move


class TestCheck_move(TestCase):
    @patch("A3.movement.check_transmat", return_value=False)
    @patch("A3.movement.check_boundaries", return_value="[]")
    def test_check_move_no_boundaries_no_transmat(self, mock_boundaries, mock_transmat):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 0, "Y-Pos": 0}
        board = {(0,0):{"Walls":[]}}
        move = "N"
        self.assertTrue(check_move(player, board, move))

    @patch("A3.movement.check_transmat", return_value=False)
    @patch("A3.movement.check_boundaries", return_value="['N']")
    def test_check_move_n_boundary_n_move(self, mock_boundaries, mock_transmat):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 0, "Y-Pos": 0}
        board = {(0, 0): {"Walls": ["N"]}}
        move = "N"
        self.assertFalse(check_move(player, board, move))

    @patch("A3.movement.check_transmat", return_value=False)
    @patch("A3.movement.check_boundaries", return_value="['N']")
    def test_check_move_n_boundary_s_move(self, mock_boundaries, mock_transmat):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 0, "Y-Pos": 0}
        board = {(0, 0): {"Walls": ["N"]}}
        move = "S"
        self.assertTrue(check_move(player, board, move))

    @patch("A3.movement.check_transmat", return_value=False)
    @patch("A3.movement.check_boundaries", return_value="['N']")
    def test_check_move_b_move(self, mock_boundaries, mock_transmat):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 0, "Y-Pos": 0}
        board = {(0, 0): {"Walls": ["N"]}}
        move = "B"
        self.assertFalse(check_move(player, board, move))

    @patch("A3.movement.check_transmat", return_value=True)
    @patch("A3.movement.check_boundaries", return_value="['N']")
    def test_check_move_yes_transmat_t_move(self, mock_boundaries, mock_transmat):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 0, "Y-Pos": 0}
        board = {(0, 0): {"Walls": ["N"]}}
        move = "T"
        self.assertTrue(check_move(player, board, move))

    @patch("A3.movement.check_transmat", return_value=False)
    @patch("A3.movement.check_boundaries", return_value="['N']")
    def test_check_move_no_transmat_t_move(self, mock_boundaries, mock_transmat):
        player = {"Name": "Donna Noble", "HP": 10, "X-Pos": 0, "Y-Pos": 0}
        board = {(0, 0): {"Walls": ["N"]}}
        move = "T"
        self.assertFalse(check_move(player, board, move))
