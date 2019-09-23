class CryptoSale(object):
    def __init__(self, id, countcoins, price, text, telephone):
        self.id = id
        self.countcoins = countcoins
        self.price = price
        self.text = text
        self.telephone = telephone

    '''
    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.countcoins, self.sumdeal, self.telephone, self.idtelegram, self.text)
    '''