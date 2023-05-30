# Define S3 Client
s3 = boto3.client(
    "s3",
    aws_access_key_id = access_key_id,
    aws_secret_access_key = secret_access_key
)

# Get object containing file to be staged
obj = s3.get_object(
    Bucket = "data-to migrate",
    Key = "iris_dataset.csv"
)

import io
import pandas as pd

# Print column info for the dataset
pd.read_csv(io.BytesIO(obj["Body"].read())).info()