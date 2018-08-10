# coding: utf-8
class Coin:
    def __init__(self, trigramme=None, devise=None, apiUrl=None, symbol=None,price=None, openDay=None, highDay=None, lowDay=None, marketCap=None, evolutionDay=None):
        self.trigramme = trigramme
        self.devise = devise
        
        if(self.devise == 'USD'):
            self.symbol = '$'
        else:
            self.symbol = self.devise
        
        self.url = apiUrl
        self.price = 0
        self.openDay = 0
        self.highDay = 0
        self.lowDay = 0
        self.marketCap = 0
        self.evolutionDay = 0
