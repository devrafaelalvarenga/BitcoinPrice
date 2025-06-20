import logging
import logging.handlers
import os
from datetime import datetime


def configurar_logging():
    """Configura o sistema de logging usando basicConfig"""

    # Criar diretório se não existir
    if not os.path.exists('bitcoinprice/logs'):
        os.makedirs('bitcoinprice/logs')

    log_file_path = 'bitcoinprice/logs/logs.log'

    # Configuração simplificada com basicConfig
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%y-%m-%d %H:%M:%S',
    )

    # Retorna o logger root ou um específico
    logger = logging.getLogger('BitcoinPriceLogger')

    # Configura o nível do logger
    logger.setLevel(logging.INFO)  # or DEBUG

    # Handler para salvar em arquivo (com rotação, para não encher o disco)
    # RotatingFileHandler: cria novos arquivos de log quando o atual atinge um tamanho
    file_handler = logging.handlers.RotatingFileHandler(
        log_file_path,
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5              # Mantém 5 arquivos de backup
    )
    file_handler.setLevel(logging.INFO)  # Nível para o arquivo de log

    # Handler para exibir no console (opcional, mas bom para monitoramento imediato)
    console_handler = logging.StreamHandler()
    # Pode ser mais verboso no console para debug
    console_handler.setLevel(logging.DEBUG)

    # Formato das mensagens
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Adiciona o formatador aos handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Adiciona os handlers ao logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
