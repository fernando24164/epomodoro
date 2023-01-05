import unittest
from click.testing import CliRunner

from src.cli import cli


class TestCLI(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = CliRunner()

    def test_start(self):
        result = self.runner.invoke(cli, ["start", "--pomor"])
        assert result.exit_code == 2
        assert "Error" in result.output

    def test_start_wrong_command(self):
        result = self.runner.invoke(cli, ["start", "-l", "quattro"])
        assert result.exit_code == 1

    def test_statistic(self):
        result = self.runner.invoke(cli, ["statistic"])
        assert result.exit_code == 0

    def test_clean(self):
        result = self.runner.invoke(cli, ["clean"])
        assert result.exit_code == 0
