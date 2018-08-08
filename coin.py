class Coin:
    def __init__(self, coinTrigramme):
        self.coinTrigramme = coinTrigramme

    def define_url(self):
        coinUrlPrice = 'https://min-api.cryptocompare.com/data/price?fsym=' + self.coinTrigramme + '&tsyms=EUR'
        return coinUrlPrice

