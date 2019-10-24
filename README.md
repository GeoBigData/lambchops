# Lambda Compiler

# Install

```console
$ pip install git+https://github.com/GeoBigData/lambchops.git@v0.0.2#egg=lambchops
```

# Usage

```console
$ lambchops build --help
Usage: lambchops build [OPTIONS] BUILD_CONTEXT OUTPUT_DIR

Options:
  --runtime [python2.7|python3.6|python3.7]
                                  The AWS Lambda runtime to use.
  --as-layer                      Whether to compile the zip file as a Lambda
                                  layer. If the flag is present, the zip
                                  archive will support uploading as a Lambda
                                  Layer. If it is not present, the zip archive
                                  will support uploading as a Lambda Function.
  --help                          Show this message and exit.
```

## Arguments

* `BUILD_CONTEXT`: This is an existing directory that contains at least a `requirements.txt` file. If you are 
also compiling custom Python code, then this must also be in the directory.
* `OUTPUT_DIR`: An existing directory into which the package will be saved. After running `lambchops build` you 
this directory will contain a `package.zip` archive and a `package` directory.

## Options

* `--runtime`: The Lambda runtime that will be used to run this function/layer. Currently only supports Python runtimes.
* `--as-layer`: Whether to compile the resources in a format suitable for an [AWS Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) 
or an AWS Lambda Function. The big difference is that for Layers, all resources will be place in a `python` directory within 
the zip archive. This allows you to simply upload the zip archive in the Lambda interface without any changes to directory structure.
 

# Examples

See the [`compile-function.sh`](examples/function/compile-function.sh) and [`compile-layer.sh`](examples/layer/compile-layer.sh) Bash 
scripts for examples of how to run for each case. 
