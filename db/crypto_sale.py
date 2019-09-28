from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.settings_db import *


Base = declarative_base()
class CryptoSale(Base):
    __tablename__ = 'cryptosale'
    id = Column(Integer, autoincrement=True, primary_key=True)
    countcoins = Column(Integer)
    price = Column(Integer)
    text = Column(String)
    telephone = Column(String)


    def __init__(self, id, countcoins, price, text, telephone):
        self.id = id
        self.countcoins = countcoins
        self.price = price
        self.text = text
        self.telephone = telephone


    '''
    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.count_coins, self.sum_deal, self.telephone, self.id_telegram, self.text)
    '''


Base.metadata.create_all(db)


