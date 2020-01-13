from unittest import TestCase
from unittest.mock import patch

from A3.movement import get_input


class TestGet_input(TestCase):
    @patch('builtins.input', return_value="n")
    def test_get_input_lowercase(self, mock_input):
        self.assertEqual(get_input(), "N")

    @patch('builtins.input', return_value="N")
    def test_get_input_uppercase(self, mock_input):
        self.assertEqual(get_input(), "N")

    @patch('builtins.input', return_value=" N ")
    def test_get_input_spaces(self, mock_input):
        self.assertEqual(get_input(), "N")
