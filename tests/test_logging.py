"""Test for IKT logging module."""
import pytest
from click.testing import CliRunner

from ikt import cli, logger


@pytest.mark.parametrize("arg_key", ("-l", "--log-level"))
@pytest.mark.parametrize(
    ("log_level", "expected_level"),
    (["DEBUG", 10], ["INFO", 20], ["WARNING", 30], ["ERROR", 40], ["CRITICAL", 50]),
)
def test_cli_logging_levels_switching(arg_key, log_level, expected_level):
    """Test logging level switching from cli."""
    runner = CliRunner()
    result = runner.invoke(cli.main_cli, args=[arg_key, log_level])

    assert result.exit_code == 0
    assert result.output == f"Logging level: {expected_level}\n"
    assert logger.level == expected_level
