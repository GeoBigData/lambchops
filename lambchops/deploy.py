import os

import click


@click.command()
@click.argument('package')
@click.argument('function_name')
def deploy(package, function_name):
    