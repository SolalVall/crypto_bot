# coding: utf-8
class Coin:
    def __init__(self, trigramme=None, devise=None, apiUrl=None, symbol=None,price=None, openDay=None, highDay=None, lowDay=None, marketCap=None, evolutionDay=None, duration=None, pourcentageDown=None, pourcentageUp=None):
        self.trigramme = trigramme
        self.devise = devise
        self.url = apiUrl
        self.price = 0
        self.openDay = 0
        self.highDay = 0
        self.lowDay = 0
        self.marketCap = 0
        self.evolutionDay = 0
        self.pourcentageHigh = 0 
        self.pourcentageLow = 0 
        self.duration = 0 

    def assign_symbol(self):
        if(self.devise == 'USD'):
            self.symbol = '$'
        elif(self.devise == 'EUR'):
            self.symbol = u"\u20AC"
        else:
            self.symbol = self.devise
