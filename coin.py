# coding: utf-8
class Coin:
    import time
    import requests
    def __init__(self, trigramme=None, devise=None, url=None, symbol=None,price=None, openDay=None, highDay=None, lowDay=None, marketCap=None, evolutionDay=None, duration=None, pourcentageDown=None, pourcentageUp=None):
        self.trigramme = trigramme
        self.devise = devise
        self.url = url
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
    
    def checkPrice(self, url, trigramme, devise, oldPrice):
        apiRequest = self.requests.get(url)
        apiRequestJson = apiRequest.json()
        updatedPrice = apiRequestJson['RAW'][trigramme][devise]['PRICE']
        return updatedPrice
        

