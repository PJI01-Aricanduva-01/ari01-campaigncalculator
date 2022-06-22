from app.models.credential import Credential



def permitir (session):
    credential = Credential.query.filter_by(credential_id=session).first()
    if credential.name == "convidado":
        x = 1
        return x
    else:
        x = 0
        return x 
    