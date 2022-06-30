from app.models.credential import Credential



def permitir (session):
    credential = Credential.query.filter_by(credential_id=session).first()
    if credential.name == "convidado":
        return True
    else:
        return False
    