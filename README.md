# Lambda Compiler

# Build

```console
$ ./build.sh
```

This will create a `build` directory with a `lambda_package` sub-directory and a `lambda_package.zip` file. The 
sub-directory is used by the `test.sh` script and the ZIP file can be uploaded to the Lambda function.

# Test

```console
$ export GBDX_USERNAME=<your_username>
$ export GBDX_PASSWORD=<your_password>
$ ./test.sh
```

# Deploy

You can upload the `build/lambda_package.zip` file into your Lambda function in the AWS console.

**You'll need to set the username and password environment variables on the function in order for gbdxtools to work.**