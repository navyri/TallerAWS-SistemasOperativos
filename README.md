<p align='center'> 
  <img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=80354A&text=Taller%20AWS&fontColor=FFFFFF&desc=Sistemas%20Operativos%20(2026-1)&fontAlignY=30&descAlignY=54"/> 
</p>

<p align='center'>
  <img src="https://64.media.tumblr.com/a6b285a68a3ce13b94b191514634ebe2/2d4a69e4bb9eff47-1a/s1280x1920/d6e4ed08a45ceba949a27893fb109d9dbd6ba362.pnj" alt="anime image" />
</p>

<p align='center'>
  <img src="https://capsule-render.vercel.app/api?type=rect&height=5&color=80354A&reversal=false&fontAlignY=40&fontColor=FFFFFF&fontSize=60"/>
</p>

# Taller AWS - Sistemas Operativos

Repositorio correspondiente al Taller AWS de la materia Sistemas Operativos, organizado en tres puntos principales.

Este repositorio contiene:

- Ejercicios de gestion de archivos en Amazon S3 usando Bash AWS CLI y boto3.
- Un despliegue de aplicacion FastAPI usando Docker.
- El desarrollo y despliegue de una aplicacion FastAPI con integracion a Amazon S3, Amazon RDS, Docker, Amazon ECR y AWS Lambda.

## Estructura general del repositorio

```bash
├── primerPunto/
│   ├── archivo.txt
│   ├── descargaS3/
│   │   └── archivo.txt
│   ├── multiplesArchivos/
│   │   ├── frase1.txt
│   │   ├── frase2.txt
│   │   ├── frase3.txt
│   │   └── descargaMultiS3/
│   └── boto3/
│       ├── archivo_boto3.txt
│       ├── s3_boto3.py
│       ├── descarga_boto3/
│       ├── descarga_frases/
│       └── multiplesArchivos/
├── segundoPunto/
│   └── test_docker_fastapi/
│       ├── Dockerfile
│       ├── main.py
│       ├── requirements.txt
│       └── run_container.sh
└── tercerPunto/
    ├── .dockerignore
    ├── .env.example
    ├── Dockerfile
    ├── requirements.txt
    └── app/
        ├── config.py
        ├── database.py
        ├── main.py
        ├── models.py
        ├── s3_utils.py
        └── schemas.py
```

<p align='center'>
  <img src="https://capsule-render.vercel.app/api?type=rect&height=5&color=80354A&reversal=false&fontAlignY=40&fontColor=FFFFFF&fontSize=60"/>
</p>

# Primer punto: gestion de archivos en Amazon S3

En el primer punto se trabajaron operaciones de almacenamiento en Amazon S3 utilizando tanto la linea de comandos con AWS CLI como scripts en Python con boto3.

Se realizaron ejercicios de:

- Creacion y uso de un bucket en Amazon S3.
- Carga de archivos individuales.
- Descarga de archivos en ubicaciones diferentes.
- Manejo de multiples archivos.
- Pruebas de carga y descarga usando boto3.

## Archivos principales del primer punto

- `primerPunto/archivo.txt`
- `primerPunto/descargaS3/archivo.txt`
- `primerPunto/multiplesArchivos/frase1.txt`
- `primerPunto/multiplesArchivos/frase2.txt`
- `primerPunto/multiplesArchivos/frase3.txt`
- `primerPunto/boto3/s3_boto3.py`

## Ejemplo de uso en Bash AWS CLI

```bash
aws s3 cp archivo.txt s3://user-xxxxxxxx-ueia-so/
aws s3 cp s3://user-xxxxxxxx-ueia-so/archivo.txt descargaS3/archivo.txt
```

## Ejemplo de uso con boto3

```bash
cd primerPunto/boto3
python s3_boto3.py
```

<p align='center'>
  <img src="https://capsule-render.vercel.app/api?type=rect&height=5&color=80354A&reversal=false&fontAlignY=40&fontColor=FFFFFF&fontSize=60"/>
</p>

# Segundo punto: despliegue de FastAPI con Docker

En el segundo punto se trabajo con una aplicacion FastAPI base ubicada en `segundoPunto/test_docker_fastapi`, la cual fue contenerizada para ejecutarse dentro de Docker.

Este punto incluye:

- Un `Dockerfile` para construir la imagen.
- El archivo `main.py` con la aplicacion FastAPI.
- Un archivo `requirements.txt` con dependencias.
- Un script `run_container.sh` para facilitar la ejecucion.

## Archivos principales del segundo punto

- `segundoPunto/test_docker_fastapi/Dockerfile`
- `segundoPunto/test_docker_fastapi/main.py`
- `segundoPunto/test_docker_fastapi/requirements.txt`
- `segundoPunto/test_docker_fastapi/run_container.sh`

## Como construir y ejecutar el segundo punto

```bash
cd segundoPunto/test_docker_fastapi

docker build -t test-docker-fastapi .
docker run -p 8000:8000 test-docker-fastapi
```

La aplicacion puede probarse en:

- `http://localhost:8000`
- `http://localhost:8000/docs`

<p align='center'>
  <img src="https://capsule-render.vercel.app/api?type=rect&height=5&color=80354A&reversal=false&fontAlignY=40&fontColor=FFFFFF&fontSize=60"/>
</p>

# Tercer punto: FastAPI + S3 + RDS + Docker + ECR + Lambda

En el tercer punto se desarrollo una aplicacion FastAPI mas completa, orientada a almacenar imagenes en Amazon S3 y registrar sus metadatos en una base de datos PostgreSQL desplegada en Amazon RDS.

La solucion incluye:

- Un endpoint `POST /upload` para recibir un usuario y una imagen en formato PNG o JPG/JPEG.
- Validacion de formatos permitidos.
- Almacenamiento del archivo en Amazon S3 organizado por usuario.
- Registro de metadatos en Amazon RDS.
- Un endpoint `GET /image` para consultar la ubicacion de la imagen y retornar una URL de acceso junto con la fecha de almacenamiento.
- Un `Dockerfile` para contenerizar la aplicacion.
- Preparacion de la imagen para ser publicada en Amazon ECR y desplegada en AWS Lambda.

## Archivos principales del tercer punto

- `tercerPunto/Dockerfile`
- `tercerPunto/requirements.txt`
- `tercerPunto/.env.example`
- `tercerPunto/app/main.py`
- `tercerPunto/app/config.py`
- `tercerPunto/app/database.py`
- `tercerPunto/app/models.py`
- `tercerPunto/app/s3_utils.py`
- `tercerPunto/app/schemas.py`

## Variables de entorno de ejemplo

El archivo `tercerPunto/.env.example` sirve como plantilla para configurar la aplicacion sin exponer credenciales reales.

Ejemplo:

```env
AWS_REGION=us-east-2
S3_BUCKET_NAME=user-xxxxxxxx-ueia-so
DATABASE_URL=postgresql://usuario:password@host:5432/talleraws
PRESIGNED_URL_EXPIRES=3600
```

## Como construir y ejecutar el tercer punto

```bash
cd tercerPunto

cp .env.example .env
docker build -t talleraws-tercerpunto-fastapi .
docker run --env-file .env -p 8000:8000 talleraws-tercerpunto-fastapi
```

La aplicacion puede probarse en:

- `http://localhost:8000/docs`

## Publicacion de imagen en ECR

Ejemplo general:

```bash
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin <ID_CUENTA>.dkr.ecr.us-east-2.amazonaws.com

docker tag talleraws-tercerpunto-fastapi:latest <ID_CUENTA>.dkr.ecr.us-east-2.amazonaws.com/so-mle-talleraws-fastapi:latest

docker push <ID_CUENTA>.dkr.ecr.us-east-2.amazonaws.com/so-mle-talleraws-fastapi:latest
```

## Despliegue en AWS Lambda

La imagen publicada en Amazon ECR se utiliza como base para crear una funcion AWS Lambda con package type `Image`, junto con una URL publica de invocacion.

<p align='center'>
  <img src="https://capsule-render.vercel.app/api?type=rect&height=5&color=80354A&reversal=false&fontAlignY=40&fontColor=FFFFFF&fontSize=60"/>
</p>

# Tecnologias utilizadas

- Amazon S3
- boto3
- AWS CLI
- FastAPI
- Python
- Docker
- PostgreSQL
- Amazon RDS
- Amazon ECR
- AWS Lambda

# Notas

- El repositorio incluye el desarrollo correspondiente a los tres puntos del taller.
- El archivo `.env` real no se versiona; solo se incluye `.env.example`.
- Las capturas de pantalla de configuracion y pruebas hacen parte de la evidencia de entrega solicitada, estas se encuentran adjuntas en el documento PDF enviado junto con este repositorio en la plataforma de entrega del trabajo.
- Para ejecutar correctamente los ejercicios con AWS, es necesario contar con credenciales configuradas y permisos sobre los servicios utilizados.

<p align='center'>
  <img src="https://capsule-render.vercel.app/api?type=rect&height=5&color=80354A&reversal=false&fontAlignY=40&fontColor=FFFFFF&fontSize=60"/>
</p>
