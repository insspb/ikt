"""This file responsible for all console interface."""
import click

from ikt import logger


@click.group(invoke_without_command=True)
@click.option(
    "-l",
    "--log-level",
    default="INFO",
    help="Set logging level.",
    type=click.Choice(
        ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=False
    ),
)
def main_cli(log_level):
    """Image Keyword Tool.

    Command line utility for image recognition and processing.
    """
    logger.setLevel(log_level.upper())

    click.echo(f"Logging level: {logger.level}")


if __name__ == '__main__':
    main_cli()
