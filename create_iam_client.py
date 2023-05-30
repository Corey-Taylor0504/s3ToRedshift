import boto3

# Create Iam client for region feeding AWS credentials extracted from the config.json
iam = boto3.client(
    "iam",
    region_name = "us-east-1",
    aws_access_key_id = access_key_id,
    aws_secret_access_key = secret_access_key
)
