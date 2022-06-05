from flask import Flask, Blueprint, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from pathlib import Path
from azure.storage.blob import BlobServiceClient
import os

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
        

    return "Retorno da Blueprint"