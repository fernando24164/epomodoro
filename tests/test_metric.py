from datetime import datetime
import unittest

from src.metrics import Metric
from src.session import Mood, Session


class TestMetric(unittest.TestCase):
    def setUp(self):
        self.metric = Metric("test")
        self.key = datetime.now().strftime("%Y-%m-%d")
        self.value = Session(120, 30, "NoName", Mood.CALM)

    def test_set_value(self):
        self.metric.set_value(self.key, self.value)
        self.assertEqual(self.metric.get_value(self.key), self.value)

    def test_get_value(self):
        self.metric.set_value(self.key, self.value)
        self.assertEqual(self.metric.get_value(self.key), self.value)

    def test_check_value_exist(self):
        self.metric.set_value(self.key, self.value)
        self.assertTrue(self.metric.check_value_exist(self.key))
