import click

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
def start(length, pomodoros, chill):
    p = Pomodoro(length=length, pomodoros=pomodoros, chill=chill)
    print(p)
    p.start()
