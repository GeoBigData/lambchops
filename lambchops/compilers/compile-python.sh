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

if [ -f /mnt/app/requirements.txt ];
then
	pip install -r /mnt/app/requirements.txt -t ${compile_dir} --upgrade;
fi

cp -r /mnt/app/* ${compile_dir}/;
rm -rf ${compile_dir}/requirements.txt;

# Remove Lambda Python packages
rm -rdf ${compile_dir}/boto3/ \
  && rm -rdf ${compile_dir}/botocore/ \
  && rm -rdf ${compile_dir}/docutils/ \
  && rm -rdf ${compile_dir}/dateutil/ \
  && rm -rdf ${compile_dir}/jmespath/ \
  && rm -rdf ${compile_dir}/s3transfer/ \
  && rm -rdf ${compile_dir}/numpy/doc/

# Remove uncompiled Python scripts
find ${compile_dir} -type f -name '*.pyc' | while read f; do n=$(echo $f | sed 's/__pycache__\///' | sed 's/.cpython-36//'); cp $f $n; done;
find ${compile_dir} -type d -a -name '__pycache__' -print0 | xargs -0 rm -rf
find ${compile_dir} -type f -a -name '*.py' -print0 | xargs -0 rm -f


cd /tmp/outputs/${OUTPUT_NAME};

zip -r ../${OUTPUT_NAME}.zip ./*;
