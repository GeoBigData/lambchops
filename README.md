# Lambda Compiler

# Install

```console
$ pip install git+https://github.com/GeoBigData/lambchops.git@v0.0.2#egg=lambchops
```

# Usage

## Build a Lambda Package

```console
$ lambchops build --help
Usage: lambchops build [OPTIONS] BUILD_CONTEXT OUTPUT_DIR

  Compiles a zip archive that can be uploaded to AWS Lambda as either a
  Function or a Layer. The BUILD_CONTEXT must contain a requirements.txt
  file that lists all of the Python dependencies. If you are compiling a
  Layer, that's all you need. If you are compiling a Function, you should
  put all of your Python code within the BUILD_CONTEXT directory as well.

Options:
  -r, --runtime [python2.7|python3.6|python3.7]
                                  The AWS Lambda runtime to use.
  -l, --as-layer                  Whether to compile the zip file as a Lambda
                                  layer. If the flag is present, the zip
                                  archive will support uploading as a Lambda
                                  Layer. If it is not present, the zip archive
                                  will support uploading as a Lambda Function.
  -o, --output-name TEXT          The name of the output zip file (and the
                                  associated folder). The zip file will be
                                  named {output_name}.zip.
  --help                          Show this message and exit.
```

### Arguments

* `BUILD_CONTEXT`: This is an existing directory that contains at least a `requirements.txt` file. If you are 
also compiling custom Python code, then this must also be in the directory.
* `OUTPUT_DIR`: An existing directory into which the package will be saved. After running `lambchops build` you 
this directory will contain a `package.zip` archive and a `package` directory.

### Options

* `--runtime`, `-r`: The Lambda runtime that will be used to run this function/layer. Currently only supports Python runtimes.
* `--as-layer`, `-l`: Whether to compile the resources in a format suitable for an [AWS Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) 
or an AWS Lambda Function. The big difference is that for Layers, all resources will be place in a `python` directory within 
the zip archive. This allows you to simply upload the zip archive in the Lambda interface without any changes to directory structure.
* `--output-name`, `-o`: A name to give the output zip file and the package directory. This should be provided *without* the file extension. 
Defaults to `package`. 
 
## Deploy a Lambda Package

```console
$ lambchops deploy --help
Usage: lambchops deploy [OPTIONS] PACKAGE

  Deploys the given zip PACKAGE as a lambda function. If no --function-name
  is given, then the function name is derived from the filename of the
  PACKAGE. The Lambda function must already exist to use this tool.

Options:
  -f, --function-name TEXT  The name of the Lambda function to update. If not
                            provided, the name of the PACKAGE file will be
                            used.
  --aws-profile TEXT        An awscli profile name to use to deploy the
                            function.
  --help                    Show this message and exit.

```

### Arguments

* `PACKAGE`: The path to a zip archive that should be used to update the Lambda function code. You can build this 
package using [`lambchops build`](#build-a-lambda-function). 

### Options

* `--function-name`, `-f`: The name of the Lambda function to update. If this option is not given, then the file name of the 
zip archive is used. For example, if you have a zip archive at `my_files/some-lambda-function.zip` then the tool will use 
`some-lambda-function` as the function name.
* `--aws-profile`: The name of an `awscli` profile to use. This should be a valid argument to the `--profile` option of the `awscli` tools.

# Examples

See the [`compile-function.sh`](examples/function/compile-function.sh) and [`compile-layer.sh`](examples/layer/compile-layer.sh) Bash 
scripts for examples of how to run for each case. 
