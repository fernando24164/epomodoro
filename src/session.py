import logging
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict

import plotext as plt

from src.metrics import Metric

logging.basicConfig(
    stream=sys.stdout, level=logging.INFO, format="[%(levelname)s] %(message)s"
)


metric_handler = Metric("statistics")


class Mood(Enum):
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"
    EXCITED = "excited"
    CALM = "calm"
    BORED = "bored"


@dataclass
class Session:
    time_in_minutes_worked: int
    time_in_minutes_chilling: int
    task_name: str
    mood: Mood

    def save(self):
        key = datetime.now().strftime("%Y-%m-%d")
        metric_handler.set_value(key, self)

    @property
    def worked_time(self):
        return self.time_in_minutes_worked

    @property
    def chilling_time(self):
        return self.time_in_minutes_chilling


class Statistics:
    """
    Class for retrieve data from shelve file
    """

    def get_data(self, num_days=7) -> Dict:
        """
        Getting data from shelve file by date range, default number of days is 7
        :param num_days: int, number of days to be returned
        :return: Dictionary of sessions
        """
        base = datetime.today()
        dates = [
            (base - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(num_days)
        ]

        answer = {}
        for date in dates:
            if metric_handler.check_value_exist(date):
                answer[date] = metric_handler.get_value(date)
        return answer

    def draw_bar(self, data: Dict):
        if data:
            working_time = [session.worked_time / 60 for session in data.values()]
            plt.title("Working hours")
            plt.bar(data.keys(), working_time, width=0.8)
            plt.show()

            chill_time = [session.chilling_time / 60 for session in data.values()]
            plt.title("Chilling hours")
            plt.bar(data.keys(), chill_time, width=0.8)
            plt.show()
        else:
            logging.info("There is no data available for this week")

    def clear_statistic(self):
        metric_handler.clean_values()
