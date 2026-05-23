import os
from dotenv import load_dotenv


load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "us-east-2")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")
PRESIGNED_URL_EXPIRES = int(os.getenv("PRESIGNED_URL_EXPIRES", "3600"))

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
ALLOWED_CONTENT_TYPES = {"image/png", "image/jpeg"}

if not S3_BUCKET_NAME:
    raise ValueError("Falta la variable de entorno S3_BUCKET_NAME")

if not DATABASE_URL:
    raise ValueError("Falta la variable de entorno DATABASE_URL")