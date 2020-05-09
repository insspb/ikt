"""
This file responsible for all console interaction functions and configuration.
"""
import click


@click.command()
def main():
    """Simple function for pip registration."""
    click.echo("Command line interface placeholder")


if __name__ == '__main__':
    main()
