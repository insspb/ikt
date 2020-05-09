"""This file responsible for all console interface."""
import click


@click.command()
def main():
    """Echo only. Project setup verification."""
    click.echo("Command line interface placeholder")


if __name__ == '__main__':
    main()
