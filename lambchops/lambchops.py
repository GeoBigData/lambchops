import click

from .build import build
from .deploy import deploy


@click.group()
def lambchops():
    pass


lambchops.add_command(build)
lambchops.add_command(deploy)
