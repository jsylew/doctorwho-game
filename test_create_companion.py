from unittest import TestCase
from unittest.mock import patch

from A3.character import create_companion


class TestCreate_companion(TestCase):
    @patch("A3.character.choose_companion", return_value="AMY POND")
    def test_create_companion(self, mock_choice):
        self.assertEqual(create_companion()["Name"][0], "AMY")
