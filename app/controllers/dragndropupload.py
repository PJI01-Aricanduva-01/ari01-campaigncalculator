from flask import Flask, Blueprint, flash, request, render_template, redirect, url_for
from sqlalchemy import and_
from werkzeug.utils import secure_filename
from pathlib import Path
from azure.storage.blob import BlobServiceClient
import os


from app import app

from config import STORAGE_ALLOWED_EXTENSIONS

from app.controllers.azure_file_controller import download_blob, upload_file_to_blob

from app.models.campaignset import Campaign_Set
from app.models.campaign import Campaign
from app.models.adset import Ad_Set
from app.models.ad import Ad
from app.models.file import *


dragndropupload = Blueprint("dragndropupload0", __name__, static_folder="static", template_folder="templates")

@dragndropupload.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('404'))

@dragndropupload.route('/uploadfile/<ad_id>', methods=['GET', 'POST'])
def uploadFile(ad_id):
    ad = Ad.query.filter_by(ad_id=ad_id).first()
    adset_id = ad.ad_set_id

    if request.method == 'POST':
        file = request.files['file']
        ext = Path(file.name).suffix
        new_file = upload_file_to_blob(file, ad)

        if not new_file:
            flash("Erro! A imagem não foi salva corretamente.")
            return redirect(url_for('adset', adset_id=adset_id))

        return redirect(url_for('adset', adset_id=adset_id))

    
@dragndropupload.route('/deletefile/<ad_id>', methods=['GET', 'POST'])
def deleteFile(ad_id):
    ad = Ad.query.filter_by(ad_id=ad_id).first()
    adset_id = ad.ad_set_id
    file = File.query.filter(and_(File.ad_id==ad_id, File.deleted==0)).all()
    if not file:
        flash("Erro: Imagem não encontrada...")
        return redirect(url_for('adset', adset_id=adset_id))
    if len(file) > 1:
        for x in file:
            x.deleted = 1
    
    file[-1].deleted = 1
    db.session.commit()

    return redirect(url_for('adset', adset_id=adset_id))

    # TODO tratar situação de quando surge uma requisição de deletar um elemento que é pai das imagens.