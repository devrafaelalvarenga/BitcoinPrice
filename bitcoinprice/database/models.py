from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import psycopg2
from bitcoinprice.database.connection import get_connection_url

# mecanismo de conexão
engine = create_engine(get_connection_url(), echo=True)
# fábrica de sessões
Session = sessionmaker(bind=engine)
# classe base para os modelos
Base = declarative_base()


# modelo para a tabela "raw_coinbase_price_btc"
class Coinbase(Base):
    __tablename__ = "raw_coinbase_price_btc"
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    base = Column(String(10))
    currency = Column(String(10))
    timestamp = Column(DateTime)
    version = Column(String(10))


# Criação da tabela no banco de dados
Base.metadata.create_all(engine)
