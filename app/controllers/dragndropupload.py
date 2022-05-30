from flask import Flask, Blueprint, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from azure.storage.blob import BlobServiceClient
import os

dragndropupload = Blueprint('dragndropupload0', __name__)

@dragndropupload.route('/')
def index():
    return "Retorno da Blueprint"