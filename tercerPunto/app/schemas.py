from datetime import datetime
from pydantic import BaseModel


class UploadResponse(BaseModel):
    id: int
    user_name: str
    image_name: str
    s3_key: str
    created_at: datetime

    class Config:
        from_attributes = True

class ImageResponse(BaseModel):
    id: int
    user_name: str
    image_name: str
    s3_key: str
    created_at: datetime
    url: str

    class Config:
        from_attributes = True