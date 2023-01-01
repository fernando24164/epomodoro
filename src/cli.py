import click

from src.session import Statistics
from src.pomodoro import Pomodoro


@click.group()
def cli():
    pass


@cli.command()
@click.option("--length", "-l", default=20, help="Length of the break in minutes.")
@click.option(
    "--pomodoros", "-p", default=4, help="Number of pomodoros for each break."
)
@click.option(
    "--chill", "-c", default=5, help="Number of minutes to chill out after each break."
)
@click.option(
    "--name-task", "-n", default="NoName", help="Task name where you are working now."
)
def start(length: int, pomodoros: int, chill: int, name_task: str) -> None:
    """Create a pomodoro session to be monitored."""
    p = Pomodoro(length=length, pomodoros=pomodoros, chill=chill, task=name_task)
    print(p)
    p.start()


@cli.command()
def statistic():
    """Print statistics of working and chilling time."""
    s = Statistics()
    s.draw_bar(s.get_data())


@cli.command()
def clean():
    """Clean statistics records"""
    s = Statistics()
    s.clear_statistic()
