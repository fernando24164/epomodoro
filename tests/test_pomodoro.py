import unittest

from src.pomodoro import Pomodoro

class TestPomodoro(unittest.TestCase):
    def test_pomodoro_length(self):
        p = Pomodoro(20, 3, 5)
        self.assertEqual(p.length, 20)
