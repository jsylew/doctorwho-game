from unittest import TestCase
from unittest.mock import patch

from A3.character import choose_companion


class TestChoose_companion(TestCase):
    @patch('builtins.input', return_value="1")
    def test_choose_companion(self, mock_input):
        self.assertEqual(choose_companion(), "AMY POND")
