"""Test for IKT cli interface."""
from click.testing import CliRunner

from ikt import cli


def test_cli_main():
    """Test cli interface placeholder."""
    runner = CliRunner()
    result = runner.invoke(cli.main_cli)
    assert result.exit_code == 0
    assert result.output == "Logging level: 20\n"
