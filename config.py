DEBUG = True

#configurando a URI para o DB do SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://campcalc_adm:eDNQ^rJ$FHTr43Z@campaigncalculator-db.mysql.database.azure.com/campcalc-db'
#string conexão SQLAlchemy para MySQL
#'mysql://username:password@localhost/db_name
#string de conexão azure:
#cnx = mysql.connector.connect(user="campcalc_adm", password="{your_password}", host="campaigncalculator-db.mysql.database.azure.com", port=3306, database="{your_database}", ssl_ca="{ca-cert filename}", ssl_disabled=False)


SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'nossa-chave-secreta-no-calc-campaign'

#alteração do path do cookie para que a session da autenticação do usuário persista entre as blueprints
SESSION_COOKIE_PATH = '/'


AZURE_VAULT_ACCOUNT = "storagecalccamp"
AZURE_STORAGE_KEY_NAME = "VL2Ag5DHfISLmOKGgnEXO6elV078ukhyhjaTx6kxVqj1ZigWrnfB7Xbx6NSfEO6AF4SkCi5rbROodPqJQlXPrQ=="
STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=storagecalccamp;AccountKey=VL2Ag5DHfISLmOKGgnEXO6elV078ukhyhjaTx6kxVqj1ZigWrnfB7Xbx6NSfEO6AF4SkCi5rbROodPqJQlXPrQ==;EndpointSuffix=core.windows.net"
STORAGE_CONTAINER = "images"
STORAGE_ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
STORAGE_MAX_CONTENT_LENGTH = 20 * 1024 * 1024    # 20 Mb limit

