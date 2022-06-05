from io import BytesIO
from pathlib import Path
from venv import create
import uuid

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobClient

from app import models

import config

ALLOWED_EXTENTIONS = ['.png', '.jpg', '.jpeg']

def create_blob_client(file_name):
    default_credential = DefaultAzureCredential()

    secret_client = SecretClient(
        vault_url=config.AZURE_VAULT_ACCOUNT, credential=default_credential
    )

    storage_credentials = secret_client.get_secret(name=config.AZURE_STORAGE_KEY_NAME)

    return BlobClient(
        account_url=config.AZURE_STORAGE_ACCOUNT,
        container_name=config.AZURE_APP_BLOB_NAME,
        blob_name=file_name,
        credential=storage_credentials.value,
    )

def check_file_ext(path):
    ext = Path(path).suffix
    return ext in ALLOWED_EXTENTIONS

def download_blob(file):
    blob_client = create_blob_client(file)
    if not blob_client.exist():
        return
    blob_content = blob_client.download_blob()
    return blob_content

def save_file_url_to_db(file_url):
    #retificar com o model e método correto
    new_file = models.File.objects.create(file_url=file_url)
    new_file.save()
    return new_file

def upload_file_to_blob(file):

    if not check_file_ext(file.name):
        return

    file_preffix = uuid.uuid4().hex
    ext = Path(file.name).suffix
    file_name = f"{file_preffix}{ext}"
    file_content = file.read()
    file_io = BytesIO(file_content)
    blob_client = create_blob_client(file_name=file_name)
    blob_client.upload_to_blob(data=file_io)
    file_object = save_file_url_to_db(blob_client.url)

    return file_object
