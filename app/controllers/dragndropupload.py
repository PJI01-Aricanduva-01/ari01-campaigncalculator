from flask import Flask, Blueprint, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from pathlib import Path
from azure.storage.blob import BlobServiceClient
import os


from app import app

dragndropupload = Blueprint("dragndropupload0", __name__, static_folder="static", template_folder="templates")

account = app.config['STORAGE_ACCOUNT_NAME']
key = app.config['STORAGE_ACCOUNT_KEY'] 
connect_str = app.config['STORAGE_CONNECTION_STRING']
container = app.config['STORAGE_CONTAINER']
extencao_permitida = app.config['STORAGE_ALLOWED_EXTENSIONS']
max_length = app.config['STORAGE_MAX_CONTENT_LENGTH']

blobServiceClient = BlobServiceClient.from_connection_string(conn_str=connect_str)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in extencao_permitida

  #solução de teste
@dragndropupload.route('/image', methods=["POST"])
def upload_images():
    if request.method == 'POST':
        image = request.files["image"]
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(filename)
            blob_client = blobServiceClient.get_blob_client(container=container, blob=filename)
            with open(filename, "rb") as data:
                try:
                    blob_client.upload_blob(data, overwrite=True)
                    msg = "Imagem enviada com Sucesso!"

                except:
                    pass
            os.remove(filename)

#solução definitiva
from app.models import ALLOWED_EXTENTIONS, download_blob, upload_file_to_blob

dragndropupload = Blueprint('dragndropupload0', __name__)

@dragndropupload.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.FILES['file']
        ext = Path(file.name).suffix
        new_file = upload_file_to_blob(file)
        if not new_file:
            return "num deu certo"
        new_file.file_name = file.name
        new_file.file_extention = ext
        new_file.save()
        
