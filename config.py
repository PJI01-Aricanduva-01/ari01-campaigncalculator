import dotenv, os

dotenv.load_dotenv()


DEBUG = True

#configurando a URI para o DB do SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.getenv('SECRET_KEY')


#alteração do path do cookie para que a session da autenticação do usuário persista entre as blueprints
SESSION_COOKIE_PATH = '/'

AZURE_STORAGE_ACCOUNT = os.getenv('AZURE_STORAGE_ACCOUNT')
AZURE_VAULT_ACCOUNT = os.getenv('AZURE_VAULT_ACCOUNT')
AZURE_STORAGE_KEY_NAME = os.getenv('AZURE_STORAGE_KEY_NAME')
AZURE_APP_BLOB_NAME = os.getenv('AZURE_APP_BLOB_NAME')


STORAGE_ALLOWED_EXTENSIONS = set(['.png', '.jpg', '.jpeg'])
STORAGE_MAX_CONTENT_LENGTH = 20 * 1024 * 1024    # 20 Mb limit


