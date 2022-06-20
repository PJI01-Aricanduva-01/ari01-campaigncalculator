import dotenv, os

dotenv.load_dotenv()

DEBUG = True

#configurando a URI para o DB do SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
#string conexão SQLAlchemy para MySQL
#'mysql://username:password@localhost/db_name
#string de conexão azure:
#cnx = mysql.connector.connect(user="campcalc_adm", password="{your_password}", host="campaigncalculator-db.mysql.database.azure.com", port=3306, database="{your_database}", ssl_ca="{ca-cert filename}", ssl_disabled=False)


SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.getenv('SECRET_KEY')
