Instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

```bash
wget "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -O "awscliv2.zip"
unzip awscliv2.zip && mv aws /usr/local/bin
sudo /usr/local/bin/aws/install
echo -e "# aws\nalias aws=/usr/local/bin/aws/aws" | tee -a ~/.bashrc
source ~/.bashrc
aws --version
```

Then setup "localstack" profile using this command

```
aws configure --profile localstack
```

Provide the following values when prompted:

* AWS Access Key ID: `test`
* AWS Secret Access Key: `test`
* Default region name: `us-east-1`
* Default output format: `json`

To create a local s3 bucket use this command:

```bash
aws --endpoint-url=http://localhost:4566 s3 mb s3://nyc-duration --profile localstack
```

Verify with this:

```bash
aws --endpoint-url=http://localhost:4566 s3 ls --profile localstack
```

Export the following enviornment variables:

```bash
export INPUT_FILE_PATTERN="s3://nyc-duration/in/{year:04d}-{month:02d}.parquet"
export OUTPUT_FILE_PATTERN="s3://nyc-duration/out/{year:04d}-{month:02d}.parquet"
export AWS_ACCESS_KEY_ID='test'
export AWS_SECRET_ACCESS_KEY='test'
export S3_ENDPOINT_URL='http://localhost:4566'
```

List files in s3 bucket 

```bash
aws --endpoint-url=http://localhost:4566 s3 ls s3://nyc-duration --recursive --human-readable --summarize
```