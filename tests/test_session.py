import pickle
import unittest
from datetime import datetime
from unittest.mock import patch

from src.metrics import Metric
from src.session import Mood, Session, Statistics


class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session(2, 2, "test", Mood.CALM)
        self.metric = Metric("test")

    def test_save_in_pickle(self):
        with open("session.pickle", "wb") as f:
            pickle.dump(self.session, f)
        with open("session.pickle", "rb") as f:
            s2 = pickle.load(f)
        self.assertEqual(self.session, s2)

    def test_save_shelve(self):
        now = str(datetime.now())
        self.metric.set_value(now, self.session)
        s = self.metric.get_value(now)
        self.assertEqual(self.session, s)


class TestStatistics(unittest.TestCase):
    def test_get_data(self):
        stats = Statistics()
        self.assertEqual(stats.get_data(), {})

    @patch("src.session.metric_handler.check_value_exist", lambda x: True)
    @patch(
        "src.session.metric_handler.get_value",
        lambda x: {
            "time_in_minutes_worked": 20,
            "time_in_minutes_chilling": 5,
            "task_name": "task1",
        },
    )
    def test_get_data_mocked(self):
        stats = Statistics()
        data = stats.get_data()
        key = datetime.now().strftime("%Y-%m-%d")
        self.assertEqual(data[key]["time_in_minutes_worked"], 20)
