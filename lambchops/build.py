import os
import sys

import click
import docker


def get_resource_path(package, resource):
    if sys.version_info >= (3,7):
        import importlib.resources

        resource_path = importlib.resources.path(package, resource)
        if not os.path.exists(resource_path):
            raise ValueError(f'Could not find resource "{resource}" in package "{package}"')
    else:
        import pkg_resources

        if not pkg_resources.resource_exists(package, resource):
            raise ValueError(f'Could not find resource "{resource}" in package "{package}"')
        return pkg_resources.resource_filename(package, resource)


@click.command()
@click.argument('build_context', type=click.Path(dir_okay=True, file_okay=False, exists=True, resolve_path=True))
@click.argument('output_dir', type=click.Path(dir_okay=True, file_okay=False, exists=True, resolve_path=True))
@click.option('--runtime', type=click.Choice(['python2.7', 'python3.6', 'python3.7']), default='python3.7', help='The AWS Lambda runtime to use. '
                                                                                                                 'Currently only supports Python runtimes.')
@click.option('--as-layer', is_flag=True, help='Whether to compile the zip file as a Lambda layer. If the flag is not present, the zip archive will support '
                                               'uploading as a Lambda Function.')
def build(build_context, output_dir, runtime, as_layer):

    client = docker.from_env()

    compilers_dir = get_resource_path('lambchops', 'compilers/')

    client.containers.run(
        f'lambci/lambda:build-{runtime}',
        f'sh -e "/src/compile-{runtime}.sh" {"layer" if as_layer else "function"}',
        volumes={
            build_context: {'bind': '/mnt/app', 'mode': 'ro'},
            output_dir: {'bind': '/tmp/outputs', 'mode': 'rw'},
            compilers_dir: {'bind': '/src', 'mode': 'ro'}
        }

    )

    pass
