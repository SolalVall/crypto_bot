class Coin:
    def __init__(self, trigramme, apiUrl, price=None, openDay=None, highDay=None, lowDay=None, marketCap=None, evolutionDay=None):
        self.trigramme = trigramme
        self.url = apiUrl
        self.price = 0
        self.openDay = 0
        self.highDay = 0
        self.lowDay = 0
        self.marketCap = 0
        self.evolutionDay = 0
