# coding: utf-8
class Coin:
    import time
    import requests
    def __init__(self, name=None, trigramme=None, devise=None, url=None, symbol=None,price=None, openDay=None, highDay=None, lowDay=None, marketCap=None, evolutionDay=None, duration=None, pourcentageDown=None, pourcentageUp=None, comparePrice=None, updatedPrice=None, variation_pourcentage=None):
        self.name = name
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
        self.updatedPrice = 0
        self.comparePrice = []
        self.variation_pourcentage = 0

    def assign_symbol(self):
        if(self.devise == 'USD'):
            self.symbol = '$'
        elif(self.devise == 'EUR'):
            self.symbol = u"\u20AC"
        else:
            self.symbol = self.devise

    def check_duration(self, duration):
        if(duration < 0):
            return 'You have to enter a positive value'
        elif(duration > 0 and duration < 5):
            return 'The minimal Bot checking duration is 5 seconds'
        else:
            return duration * 1000

    def update_price(self, url, trigramme, devise):
        apiRequest = self.requests.get(url)
        apiRequestJson = apiRequest.json()
        self.updatedPrice = apiRequestJson['RAW'][trigramme][devise]['PRICE']
        return self.updatedPrice

    def price_variation(self, comparePrice):
        self.variation_pourcentage = (float(comparePrice[-1]-comparePrice[0])/float(comparePrice[0]))*100
        return self.variation_pourcentage
       
