from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_string = "postgresql://postgres:45091847@localhost/cracc"
db = create_engine(db_string)
Session = sessionmaker(bind=db)
session = Session()




Base = declarative_base()
class BotDeals(Base):
    __tablename__ = 'botdeal'
    id = Column(Integer, autoincrement=True, primary_key=True)
    countcoins = Column(Integer)
    sumdeal = Column(Integer)
    telephone = Column(String)
    idtelegram = Column(String)
    text = Column(String)


    def __init__(self, countcoins, sumdeal, telephone, idtelegram, text):
        self.countcoins = countcoins
        self.sumdeal = sumdeal
        self.telephone = telephone
        self.idtelegram = idtelegram
        self.text = text


    '''
    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.count_coins, self.sum_deal, self.telephone, self.id_telegram, self.text)
    '''


Base.metadata.create_all(db)
