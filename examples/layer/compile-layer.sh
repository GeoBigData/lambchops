#!/bin/bash

mkdir -p ./build;
rm -rf ./build/*;
lambchops build ./context/ ./build/ --runtime python3.6 --as-layer --output-name test-layer;
