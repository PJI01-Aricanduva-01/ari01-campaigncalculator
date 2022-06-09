from io import BytesIO
from pathlib import Path
from venv import create
import uuid

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobClient

from app.models.file import *

import config

def create_blob_client(file_name):
    storage_credentials = config.AZURE_STORAGE_KEY_NAME

    return BlobClient(
        account_url=config.AZURE_STORAGE_ACCOUNT,
        container_name=config.AZURE_APP_BLOB_NAME,
        blob_name=file_name,
        credential=storage_credentials,
    )

def check_file_ext(path):
    ext = Path(path).suffix
    return ext in config.STORAGE_ALLOWED_EXTENSIONS

def download_blob(file):
    blob_client = create_blob_client(file)
    if not blob_client.exist():
        return
    blob_content = blob_client.download_blob()
    return blob_content

def save_file_url_to_db(file_name ,file_url, ext, ad_id):
    #retificar com o model e método correto
    file = File(file_name, file_url, ext, ad_id)
    db.session.add(file)
    db.session.commit()
    return db.session

def upload_file_to_blob(file, ad):

    if not check_file_ext(file.filename):
        return

    file_preffix = uuid.uuid4().hex
    ext = Path(file.filename).suffix
    file_name = f"{file_preffix}{ext}"
    file_content = file.read()
    file_io = BytesIO(file_content)
    blob_client = create_blob_client(file_name=file_name)
    blob_client.upload_blob(data=file_io)
    file_object = save_file_url_to_db(file_name, blob_client.url, ext, ad.ad_id)

    return file_object
