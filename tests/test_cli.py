"""Test for IKT cli interface."""
from click.testing import CliRunner

from ikt import cli


def test_cli_main():
    """Test cli interface placeholder."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert result.output == "Command line interface placeholder\n"
