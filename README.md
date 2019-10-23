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