from unittest import TestCase
from A3.movement import check_quit


class TestCheck_quit(TestCase):
    def test_check_quit_Q(self):
        self.assertTrue(check_quit("Q"))

    def test_check_quit_not_Q(self):
        self.assertFalse(check_quit("E"))
