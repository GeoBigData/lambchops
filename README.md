# Lambda Compiler

# Install

```console
$ pip install git+https://github.com/GeoBigData/lambchops.git
```

# Examples

```console
$ git clone https://github.com/GeoBigData/lambchops.git
$ cd lambchops
$ mkdir ./examples/function/build
$ lambchops build ./examples/function/context/ ./examples/function/build --runtime python3.6
$ mkdir ./examples/layer/build
$ lambchops build ./examples/layer/context/ ./examples/layer/build --runtime python3.7 --as-layer
```

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
