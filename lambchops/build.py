import importlib_resources
import click
import docker

COMPILER_MAPPING = {
    'python2.7': 'compile-python.sh',
    'python3.6': 'compile-python.sh',
    'python3.7': 'compile-python.sh'
}


@click.command()
@click.argument('build_context', type=click.Path(dir_okay=True, file_okay=False, exists=True, resolve_path=True))
@click.argument('output_dir', type=click.Path(dir_okay=True, file_okay=False, exists=True, resolve_path=True))
@click.option('--runtime', '-r', type=click.Choice(['python2.7', 'python3.6', 'python3.7']), default='python3.7', help='The AWS Lambda runtime to use.')
@click.option('--as-layer', '-l', is_flag=True, help='Whether to compile the zip file as a Lambda layer. If the flag is present, the zip archive will support '
                                               'uploading as a Lambda Layer. If it is not present, the zip archive will support uploading as a Lambda Function.')
@click.option('--output-name', '-o', default='package', help='The name of the output zip file (and the associated folder). The zip file will be named {output_name}.zip.')
@click.option('--image', '-i', help='The Docker image to use when building the layer/function. Defaults to one of the lambci/lambda:build-* images.')
def build(build_context, output_dir, runtime, as_layer, output_name, image):
    """
    Compiles a zip archive that can be uploaded to AWS Lambda as either a Function or a Layer. The BUILD_CONTEXT must contain a requirements.txt file that lists
    all of the Python dependencies. If you are compiling a Layer, that's all you need. If you are compiling a Function, you should put all of your Python code
    within the BUILD_CONTEXT directory as well.
    """

    client = docker.from_env()

    compilers_dir = importlib_resources.files('lambchops').joinpath('compilers')
    compiler_name = COMPILER_MAPPING[runtime]

    image = image or f'lambci/lambda:build-{runtime}'

    client.containers.run(
        image,
        f'sh -e "/src/{compiler_name}" {"layer" if as_layer else "function"} "{output_name}"',
        volumes={
            build_context: {'bind': '/mnt/app', 'mode': 'ro'},
            output_dir: {'bind': '/tmp/outputs', 'mode': 'rw'},
            compilers_dir: {'bind': '/src', 'mode': 'ro'}
        }

    )
