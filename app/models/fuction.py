from flask import flash
from app.models.credential import Credential



def permitir (session):
    credential = Credential.query.filter_by(credential_id=session).first()
    if credential.name == "convidado":
        flash("Você não tem permissão do Responsável da agencia para acessa as campanhas. \n Entre em contato com Responsável")
        return False
    else:
        return True 
    