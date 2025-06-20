import requests
from datetime import datetime
from utils import logging, configurar_logging

# Define o nome do logger
logger_name: str = 'BitcoinPriceLogger.bitcoinprice.tests.test_extract'
# Define o logger para o módulo atual
logger: str = logging.getLogger(logger_name)


def extract() -> dict:
    """
    Testa a extração de dados da API Coinbase.

    Esta função realiza uma requisição GET para a API de preços spot do Coinbase,
    verifica se a resposta contém os campos esperados e adiciona metadados como timestamp
    e versão. Em caso de erro de conexão, timeout, erro HTTP ou outras exceções de requisição,
    imprime uma mensagem de erro e retorna None.

    Returns:
        dict or None: Dicionário com os dados extraídos e metadados, ou None em caso de erro.
    """
    logger.info("Iniciando a extração dos dados da API - Coinbase.")

    url_api: str = "https://api.coinbase.com/v2/prices/spot"
    version: str = '1.0'
    try:
        response: str = requests.get(url_api)
        raw_data: dict = response.json()
        if 'data' in raw_data and 'amount' in raw_data['data'] and 'base' in raw_data['data'] and 'currency' in raw_data['data']:
            if 'metadata' not in raw_data:
                raw_data['metadata'] = {}
            raw_data['metadata']['timestamp'] = datetime.now().isoformat()
            raw_data['metadata']['version'] = version
            logger.info("Dados extraídos com sucesso")
            return raw_data
        else:
            logger.error("Resposta inesperada da API: %s", raw_data)
            print("Unexpected response format:", raw_data)
            return None
    except requests.excepitions.ConnectionError as ConnectionError:
        logger.error("Erro de conexão: %s", ConnectionError)
        print(f"Connection error:", {ConnectionError})
        return None
    except requests.exceptions.ConnectTimeout as ConnectTimeout:
        logger.error("Tempo de conexão esgotado: %s", ConnectTimeout)
        print(f"Connection timed out:", {ConnectTimeout})
        return None
    except requests.exceptions.HTTPError as HTTPError:
        logger.error("Erro HTTP: %s", HTTPError)
        print(f"HTTP error:", {HTTPError})
        return None
    except requests.exceptions.RequestException as RequestException:
        logger.error("Erro de requisição: %s", RequestException)
        print(f"Request exception:", {RequestException})
        return None


# if __name__ == '__main__':
#     extract = extract()
#     print(extract)
