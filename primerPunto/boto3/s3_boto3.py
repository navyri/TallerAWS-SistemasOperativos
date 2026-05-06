import boto3
from botocore.exceptions import ClientError
import os

BUCKET_NAME = "user-1020302250-ueia-so"
AWS_REGION = "us-east-2"

def create_s3_client():
    return boto3.client("s3", region_name=AWS_REGION)

def upload_file_with_boto3(local_path, key):
    s3_client = create_s3_client()

    if not os.path.exists(local_path):
        print(f"Error: el archivo local no existe -> {local_path}")
        return

    try:
        s3_client.upload_file(local_path, BUCKET_NAME, key)
        print(f"Archivo subido: {local_path} -> s3://{BUCKET_NAME}/{key}")
    except ClientError as e:
        print("Error al subir:", e)

def download_file_with_boto3(key, download_path):
    s3_client = create_s3_client()

    try:
        os.makedirs(os.path.dirname(download_path), exist_ok=True)
        s3_client.download_file(BUCKET_NAME, key, download_path)
        print(f"Archivo descargado: s3://{BUCKET_NAME}/{key} -> {download_path}")
    except ClientError as e:
        print("Error al descargar:", e)

def prueba_general(rutas_locales, carpeta_s3, carpeta_descarga):
    for ruta in rutas_locales:
        nombre_archivo = os.path.basename(ruta)
        key = f"{carpeta_s3}/{nombre_archivo}"
        upload_file_with_boto3(ruta, key)

    s3_client = create_s3_client()
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix=f"{carpeta_s3}/")
        print(f"Objetos bajo {carpeta_s3}/:")
        for obj in response.get("Contents", []):
            print(obj["Key"])
    except ClientError as e:
        print("Error al listar objetos:", e)

    os.makedirs(carpeta_descarga, exist_ok=True)

    for ruta in rutas_locales:
        nombre_archivo = os.path.basename(ruta)
        key = f"{carpeta_s3}/{nombre_archivo}"
        destino_local = os.path.join(carpeta_descarga, nombre_archivo)
        download_file_with_boto3(key, destino_local)

    print(f"Contenido de los archivos descargados en {carpeta_descarga}/:")
    for ruta in rutas_locales:
        nombre_archivo = os.path.basename(ruta)
        ruta_descargada = os.path.join(carpeta_descarga, nombre_archivo)
        if os.path.exists(ruta_descargada):
            with open(ruta_descargada, "r", encoding="utf-8") as f:
                print(f"{nombre_archivo} -> {f.read()}")
        else:
            print(f"No se encontro {ruta_descargada}")

def main():
    archivo_unico = "archivo_boto3.txt"
    if not os.path.exists(archivo_unico):
        with open(archivo_unico, "w", encoding="utf-8") as f:
            f.write("Este archivo fue creado para la prueba de un solo archivo con boto3.")

    rutas_un_archivo = [archivo_unico]
    print("PRUEBA CON UN SOLO ARCHIVO")
    prueba_general(rutas_un_archivo, "boto3", "descarga_boto3")

    carpeta_frases = "multiplesArchivos"
    os.makedirs(carpeta_frases, exist_ok=True)

    rutas_frases = []
    frases = [
        ("frase1.txt", "Praise the Sun!"),
        ("frase2.txt", "I wish to pay proper respect with that soul."),
        ("frase3.txt", "I am Malenia, Blade of Miquella, and I have never known defeat.")
    ]

    for nombre_archivo, contenido in frases:
        ruta = os.path.join(carpeta_frases, nombre_archivo)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
        rutas_frases.append(ruta)

    print("\nPRUEBA CON TRES ARCHIVOS")
    prueba_general(rutas_frases, "archivos", "descarga_frases")

if __name__ == "__main__":
    main()
