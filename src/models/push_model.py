import boto3
import shutil
from botocore.exceptions import NoCredentialsError

def upload_to_s3(local_model_path,bucket_name, s3_file_path):
    # Create an S3 client
    # s3 = boto3.client('s3')
    s3=boto3.resource(
    service_name='s3',
    region_name="eu-north-1",
    )

    try:
        # Upload the file
        s3.Bucket(bucket_name).upload_file(Filename= s3_file_path,Key=local_model_path)
        print(f"File uploaded successfully to {bucket_name}/{s3_file_path}")
    except FileNotFoundError:
        print(f"The file {local_model_path} was not found.")
    except NoCredentialsError:
        print("Credentials not available.")

# Example usage
local_model_path = 'models/model.joblib'
s3_bucket_name = 'mybucketqadeer'
s3_file_path = 'models/model.joblib' 

upload_to_s3(local_model_path,s3_bucket_name, s3_file_path)
shutil.copy(local_model_path, 'model.joblib')