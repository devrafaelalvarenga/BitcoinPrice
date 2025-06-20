from dotenv import load_dotenv
import psycopg2
import os
from utils import configurar_logging, logging

log = configurar_logging()
# Define o nome do logger
logger_name = 'BitcoinPriceLogger.bitcoinprice.database.connection'
# Define o logger para o módulo atual
logger = logging.getLogger(logger_name)


# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração usando variáveis de ambiente
db_config = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}


def get_connection_url():
    """
    Função para obter uma conexão com o banco de dados PostgreSQL.

    Retorna:
        conn: Conexão com o banco de dados.
    """

    try:
        conn = psycopg2.connect(
            host=db_config['host'],
            port=db_config['port'],
            database=db_config['database'],
            user=db_config['user'],
            password=db_config['password']
        )
        conn_db = (
            f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")
        logger.info("Conexão com o banco de dados estabelecida com sucesso.")
        return conn_db
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        logger.error(f"Erro ao conectar ao banco de dados: {e}")
        raise


# if __name__ == "__main__":
#     try:
#         connection = get_db_connection()
#         print("Conexão com o banco de dados estabelecida com sucesso.")
#         connection.close()
#     except Exception as e:
#         print(f"Erro ao estabelecer conexão: {e}")
