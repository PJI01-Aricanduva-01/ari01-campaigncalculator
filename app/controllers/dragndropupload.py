from flask import Flask, Blueprint, flash, request, render_template, redirect, url_for
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
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('não tem arquivo')
            return redirect(url_for('index'))
        file = request.files['file']
        file_name = file.filename
        return "Deu Quase" + file_name

    return "Sem Arquivo"

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
            return "num deu certo"

        adset = Ad_Set.query.filter_by(ad_set_id=adset_id).first()
        campaign = Campaign.query.filter_by(campaign_id=adset.campaign_id).first() #consulta dos detalhes de campanha
        campaign_set = Campaign_Set.query.filter_by(campaign_set_id=campaign.campaign_set_id).first()
        ad = Ad.query.filter_by(ad_set_id=adset_id)
        return render_template('adset.html', adset=adset, ad=ad, campaign=campaign, campset=campaign_set)

    
@dragndropupload.route('/deletefile/<ad_id>', methods=['GET', 'POST'])
def deleteFile(ad_id):
    ad = Ad.query.filter_by(ad_id=ad_id).first()
    adset_id = ad.ad_set_id
    file = File.query.filter_by(ad_id=ad_id).first()
    if not file:
        flash("Erro: Imagem não encontrada...")
        return redirect(url_for('adset', adset_id=adset_id))
    file.deleted = 1
    db.session.commit()
    #file = File.query.filter_by(ad_id=ad_id).first().update({ File.deleted : 1 })

    adset = Ad_Set.query.filter_by(ad_set_id=adset_id).first()
    campaign = Campaign.query.filter_by(campaign_id=adset.campaign_id).first() #consulta dos detalhes de campanha
    campaign_set = Campaign_Set.query.filter_by(campaign_set_id=campaign.campaign_set_id).first()
    ad = Ad.query.filter_by(ad_set_id=adset_id)
    return render_template('adset.html', adset=adset, ad=ad, campaign=campaign, campset=campaign_set)

