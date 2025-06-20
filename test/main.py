if __name__ == '__main__':
    from bitcoinprice import configurar_logging

    # 1. Configura o logger principal uma única vez
    logger_principal = configurar_logging()
    logger_principal.info("Configuração do logger principal realizada.")
