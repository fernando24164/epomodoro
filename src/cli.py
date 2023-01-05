import click
from click import ParamType
from click.shell_completion import CompletionItem

from src.pomodoro import Pomodoro
from src.session import Statistics


class LenCompletion(ParamType):
    name = "len_completion"

    def shell_complete(self, ctx, param, incomplete):
        return [CompletionItem(time_period) for time_period in (10, 15, 20)]


class PomodoroCompletion(ParamType):
    name = "pomodo_completion"

    def shell_complete(self, ctx, param, incomplete):
        return [CompletionItem(pomodoros) for pomodoros in (1, 2, 4)]


class ChillCompletion(ParamType):
    name = "chill_completion"

    def shell_complete(self, ctx, param, incomplete):
        return [CompletionItem(time_period) for time_period in (1, 5, 10)]


class TaskCompletion(ParamType):
    name = "task_completion"

    def shell_complete(self, ctx, param, incomplete):
        return [
            CompletionItem(task_name)
            for task_name in ("Task1", "NoName", "CoolTask")
        ]


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--length",
    "-l",
    type=LenCompletion(),
    default=20,
    help="Length of the break in minutes.",
)
@click.option(
    "--pomodoros",
    "-p",
    type=PomodoroCompletion(),
    default=4,
    help="Number of pomodoros for each break.",
)
@click.option(
    "--chill",
    "-c",
    type=ChillCompletion(),
    default=5,
    help="Number of minutes to chill out after each break.",
)
@click.option(
    "--name-task",
    "-n",
    type=TaskCompletion(),
    default="NoName",
    help="Task name where you are working now.",
)
def start(length: int, pomodoros: int, chill: int, name_task: str) -> None:
    """Create a pomodoro session to be monitored."""
    p = Pomodoro(length=length, pomodoros=pomodoros, chill=chill, task=name_task)
    print(p)
    p.start()


@cli.command(help="Print statistics about the sessions in a period of a wek")
def statistic():
    """Print statistics of working and chilling time."""
    s = Statistics()
    s.draw_bar(s.get_data())


@cli.command(help="Clean statistics records")
def clean():
    """Clean statistics records"""
    s = Statistics()
    s.clear_statistic()
