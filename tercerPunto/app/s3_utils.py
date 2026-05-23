import boto3
from app.config import AWS_REGION, S3_BUCKET_NAME, PRESIGNED_URL_EXPIRES


def get_s3_client():
    return boto3.client("s3", region_name=AWS_REGION)

def upload_bytes_to_s3(file_bytes, key, content_type):
    s3_client = get_s3_client()
    s3_client.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=key,
        Body=file_bytes,
        ContentType=content_type
    )

def generate_presigned_url(key):
    s3_client = get_s3_client()
    return s3_client.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": S3_BUCKET_NAME,
            "Key": key
        },
        ExpiresIn=PRESIGNED_URL_EXPIRES
    )