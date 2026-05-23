from pathlib import Path

from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app.models import ImageRecord
from app.schemas import UploadResponse, ImageResponse
from app.s3_utils import upload_bytes_to_s3, generate_presigned_url
from app.config import ALLOWED_EXTENSIONS, ALLOWED_CONTENT_TYPES


app = FastAPI(title="Taller AWS - Punto 3")

Base.metadata.create_all(bind=engine)

def validate_image(file: UploadFile) -> str:
    if not file.filename:
        raise HTTPException(status_code=400, detail="El archivo debe tener un nombre valido")

    extension = Path(file.filename).suffix.lower().replace(".", "")

    if not extension:
        raise HTTPException(status_code=400, detail="El archivo debe tener una extension valida")

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=415, detail="Formato no permitido. Solo PNG, JPG o JPEG")

    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=415, detail="Tipo MIME no permitido. Solo image/png o image/jpeg")

    return extension


@app.get("/")
def root():
    return {"message": "Punto 3 activo"}


@app.post("/upload", response_model=UploadResponse)
async def upload_image(
    user_name: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    clean_user_name = user_name.strip()

    if not clean_user_name:
        raise HTTPException(status_code=400, detail="El nombre del usuario es obligatorio")

    validate_image(file)

    file_bytes = await file.read()

    if not file_bytes:
        raise HTTPException(status_code=400, detail="El archivo esta vacio")

    image_name = Path(file.filename).name
    s3_key = f"{clean_user_name}/{image_name}"

    try:
        upload_bytes_to_s3(file_bytes, s3_key, file.content_type)
    except Exception:
        raise HTTPException(status_code=500, detail="Error subiendo imagen a S3")

    new_record = ImageRecord(
        user_name=clean_user_name,
        image_name=image_name,
        s3_key=s3_key
    )

    try:
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error guardando registro en RDS")

    return new_record


@app.get("/image", response_model=ImageResponse)
def get_image(
    user_name: str,
    image_name: str,
    db: Session = Depends(get_db)
):
    clean_user_name = user_name.strip()
    clean_image_name = image_name.strip()

    if not clean_user_name or not clean_image_name:
        raise HTTPException(status_code=400, detail="user_name e image_name son obligatorios")

    record = db.query(ImageRecord).filter(
        ImageRecord.user_name == clean_user_name,
        ImageRecord.image_name == clean_image_name
    ).first()

    if not record:
        raise HTTPException(status_code=404, detail="Usuario o imagen no encontrados")

    try:
        url = generate_presigned_url(record.s3_key)
    except Exception:
        raise HTTPException(status_code=500, detail="Error generando URL prefirmada")

    return ImageResponse(
        id=record.id,
        user_name=record.user_name,
        image_name=record.image_name,
        s3_key=record.s3_key,
        created_at=record.created_at,
        url=url
    )