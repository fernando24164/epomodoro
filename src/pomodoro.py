import logging
import time
from pathlib import Path

import click
from src.session import Mood, Session

# To avoid display playsound warning log about dependencies
logging.getLogger("playsound").setLevel(logging.CRITICAL)
from playsound import playsound

media_dir = f"{str(Path.cwd())}/src/media/sounds/"


class Pomodoro:
    def __init__(
        self, length: int = 30, pomodoros: int = 4, chill: int = 5, task: str = "NoName"
    ) -> None:
        self.length = int(length)
        self.pomodoros = int(pomodoros)
        self.chill = int(chill)
        self.session = Session(
            time_in_minutes_worked=0,
            time_in_minutes_chilling=0,
            task_name=task,
            mood=Mood.CALM,
        )

    def start(self) -> None:
        """start pomodoro timer"""
        click.secho("Pomodoro started Get focus! Happy pomodoro!", bold=True)
        for _ in range(self.pomodoros):
            self.display_work_timer()
            self.display_chillout_timer()

    def play_sound(self):
        playsound(media_dir + "finish_task.wav")

    def display_work_timer(self):
        for time_passed in range(0, self.length, 1):
            click.secho("*" * (self.length - time_passed), fg="blue", bold=True)
            time.sleep(60)
            self.session.time_in_minutes_worked += 1
        self.session.save()
        self.play_sound()

    def display_chillout_timer(self):
        click.secho("Time to chill out", bold=True)
        for time_passed in range(0, self.chill, 1):
            click.secho("*" * (self.chill - time_passed), fg="green", bold=True)
            time.sleep(60)
            self.session.time_in_minutes_chilling += 1
        self.session.save()
        self.play_sound()

    def __str__(self) -> str:
        return f"Pomodoro (length={self.length} minutes, pomodoros={self.pomodoros}, chill={self.chill} minutes)"


class TermDrawer:
    """
    Class to generate terminal plots using plotext
    """

    def __init__(self, metrics, metric_name: str):
        self.metrics = metrics
        self.metric_name = metric_name
