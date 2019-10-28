import os

import click
import boto3
import botocore.exceptions


@click.command()
@click.argument('package', type=click.File('rb'))
@click.option('--function-name', '-f', help='The name of the Lambda function to update. If not provided, the name of the PACKAGE file will be used.')
@click.option('--aws-profile', help='An awscli profile name to use to deploy the function.')
def deploy(package, function_name, aws_profile):
    """
    Deploys the given zip PACKAGE as a lambda function. If no --function-name is given, then the function name is derived from the filename of the PACKAGE.
    The Lambda function must already exist to use this tool.
    """
    if aws_profile:
        session = boto3.Session(profile_name=aws_profile)
        lambda_client = session.client('lambda')
    else:
        lambda_client = boto3.client('lambda')

    # Get the function name from the option or the package filename
    function_name = function_name or os.path.splitext(os.path.basename(package.name))[0]

    try:
        lambda_client.update_function_code(
            FunctionName=function_name,
            ZipFile=package.read()
        )
        click.secho(
            f'Successfully deployed {package.name} to function {function_name}'
        )
    except botocore.exceptions.ClientError as e:
        boto_error = e.response.get('Error')
        
        if boto_error and boto_error['Code'] == 'ResourceNotFoundException':
            return click.secho(f'No function named {function_name} found in {lambda_client._client_config.region_name} region. '
                               f'Please use the --function-name argument to specify a function name.', fg='red')
        raise
