DEBUG = True

#configurando a URI para o DB do SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://campcalc_adm:eDNQ^rJ$FHTr43Z@campaigncalculator-db.mysql.database.azure.com/campcalc-db'
#string conexão SQLAlchemy para MySQL
#'mysql://username:password@localhost/db_name
#string de conexão azure:
#cnx = mysql.connector.connect(user="campcalc_adm", password="{your_password}", host="campaigncalculator-db.mysql.database.azure.com", port=3306, database="{your_database}", ssl_ca="{ca-cert filename}", ssl_disabled=False)


SQLALCHEMY_TRACK_MODIFICATIONS = True

SESSION_TYPE = 'null'


SECRET_KEY = 'nossa-chave-secreta-no-calc-campaign'
