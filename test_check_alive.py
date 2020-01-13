from unittest import TestCase

from A3.fight import check_alive


class TestCheck_alive(TestCase):
    def test_check_alive_yes(self):
        player = {"HP": 5}
        self.assertTrue(check_alive(player))

    def test_check_alive_no(self):
        player = {"HP": 0}
        self.assertFalse(check_alive(player))