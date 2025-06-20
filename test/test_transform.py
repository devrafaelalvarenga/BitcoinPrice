from .test_extract import extract
from datetime import datetime
from bitcoinprice.database.models import Coinbase
from utils import logging, configurar_logging

# Define o nome do logger
logger_name: str = 'BitcoinPriceLogger.bitcoinprice.tests.test_transform'
# Define o logger para o módulo atual
logger: str = logging.getLogger(logger_name)


# Função para transformar os dados extraídos em um objeto do modelo Coinbase
def transform(raw_data):
    """
    Transforma os dados brutos extraídos da API Coinbase em um objeto do modelo Coinbase.
    Args:
        raw_data (dict): Dados brutos extraídos da API.
    Returns:
        Coinbase: Objeto do modelo Coinbase com os dados transformados.
    """
    logger.info("Iniciando a transformaçao dos dados extraidos.")

    if not raw_data or 'data' not in raw_data:
        logger.error("Dados brutos inválidos ou ausentes.")
        raise ValueError("Dados brutos inválidos ou ausentes.")

    # Extrai os dados necessários do dicionário raw_data
    if 'amount' not in raw_data['data'] or 'base' not in raw_data['data'] or 'currency' not in raw_data['data']:
        logger.error(
            "Dados brutos incompletos: 'amount', 'base' ou 'currency' ausentes.")
        raise ValueError(
            "Dados brutos incompletos: 'amount', 'base' ou 'currency' ausentes.")
    else:
        # Cria um objeto Coinbase com os dados extraídos
        amount = float(raw_data['data']['amount'])
        base = str(raw_data['data']['base'])
        currency = str(raw_data['data']['currency'])
        timestamp = datetime.fromisoformat(raw_data['metadata']['timestamp'])
        version = str(raw_data['metadata']['version'])
        data = Coinbase(amount=amount, base=base,
                        currency=currency, timestamp=timestamp, version=version)
        logger.info("Dados transformados com sucesso.")
        return data


# if __name__ == '__main__':
#     extracted_data = extract()
#     transform_data = transform(extracted_data)
#     # print(transform)
