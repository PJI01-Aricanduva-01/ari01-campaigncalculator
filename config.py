import dotenv, os

dotenv.load_dotenv()


DEBUG = True

#configurando a URI para o DB do SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://campcalc_adm:eDNQ^rJ$FHTr43Z@calculatorcampaign-db.mysql.database.azure.com/campcalc'

SQLALCHEMY_TRACK_MODIFICATIONS = True

SESSION_TYPE = 'null'


SECRET_KEY = 'nossa-chave-secreta-no-calc-campaign'

#alteração do path do cookie para que a session da autenticação do usuário persista entre as blueprints
SESSION_COOKIE_PATH = '/'

AZURE_STORAGE_ACCOUNT = os.getenv('AZURE_STORAGE_ACCOUNT')
AZURE_VAULT_ACCOUNT = os.getenv('AZURE_VAULT_ACCOUNT')
AZURE_STORAGE_KEY_NAME = os.getenv('AZURE_STORAGE_KEY_NAME')
AZURE_APP_BLOB_NAME = os.getenv('AZURE_APP_BLOB_NAME')


STORAGE_CONTAINER = "images"
STORAGE_ALLOWED_EXTENSIONS = set(['.png', '.jpg', '.jpeg'])
STORAGE_MAX_CONTENT_LENGTH = 20 * 1024 * 1024    # 20 Mb limit

