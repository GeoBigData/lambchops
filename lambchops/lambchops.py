import click

from .build import build


@click.group()
def lambchops():
    pass


lambchops.add_command(build)
