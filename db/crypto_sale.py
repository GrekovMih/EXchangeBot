class CryptoSale(object):
    def __init__(self, id, count_coins, price, text, telephone):
        self.id = id
        self.count_coins = count_coins
        self.price = price
        self.text = text
        self.telephone = telephone

    '''
    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.count_coins, self.sum_deal, self.telephone, self.id_telegram, self.text)
    '''