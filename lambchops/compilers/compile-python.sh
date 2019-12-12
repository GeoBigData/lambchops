#!/bin/bash

COMPILE_TYPE=$1;
OUTPUT_NAME=$2;

zip_name="/tmp/outputs/${OUTPUT_NAME}";

if [ $COMPILE_TYPE == 'layer' ]; then
	compile_dir="${zip_name}/python";
else
	compile_dir=${zip_name};
fi

rm -rf ${zip_name}.zip;
rm -rf ${zip_name};

mkdir -p ${compile_dir};

if [[ -f /mnt/app/requirements.txt ]];
then
	pip install -r /mnt/app/requirements.txt -t ${compile_dir} --upgrade;
fi

cp -r /mnt/app/* ${compile_dir}/;
rm -rf ${compile_dir}/requirements.txt;

cd /tmp/outputs/${OUTPUT_NAME};

zip -r ../${OUTPUT_NAME}.zip ./*;
