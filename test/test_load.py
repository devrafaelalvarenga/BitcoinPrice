from test.test_extract import extract
from test.test_transform import transform
from bitcoinprice.database.models import Session
from utils import logging, configurar_logging

# Define o nome do logger
logger_name: str = 'BitcoinPriceLogger.bitcoinprice.tests.test_load'
# Define o logger para o módulo atual
logger: str = logging.getLogger(logger_name)


def load(updated_data):
    with Session() as session:
        session.add(updated_data)
        session.commit()


if __name__ == '__main__':
    extracted_data = extract()
    transform_data = transform(extracted_data)
    logger.info("Iniciado a inserçao dos dados no banco de dados.")
    load(transform_data)
    logger.info("Dados carregados com sucesso no banco de dados.")
