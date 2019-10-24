#!/bin/bash

COMPILE_TYPE=$1;

if [ $COMPILE_TYPE == 'layer' ]; then
	compile_dir="/tmp/outputs/package/python";
else
	compile_dir="/tmp/outputs/package";
fi

rm -rf /tmp/outputs/package.zip;
rm -rf ${compile_dir};

mkdir -p ${compile_dir};
pip install -r /mnt/app/requirements.txt -t ${compile_dir} --upgrade;

cp /mnt/app/* ${compile_dir}/;
rm -rf ${compile_dir}/requirements.txt;

cd /tmp/outputs/package;

zip -r ../package.zip ./*;
