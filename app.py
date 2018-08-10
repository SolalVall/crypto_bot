#!/usr/bin/python
import requests
import json
import time
from coin import Coin
from flask import Flask, render_template, request

app = Flask(__name__)
selected_crypto = Coin()

@app.route('/', methods=['POST','GET'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['bttnInfo'] == 'Get Info':
            coinTrigramme = request.form['cryptoTrigramme']
            coinDevise = request.form['cryptoDevise'] 
            apiUrl = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + coinTrigramme + '&tsyms=' + coinDevise
            #selected_crypto = Coin(coinTrigramme, coinDevise, apiUrl)
            selected_crypto.trigramme = coinTrigramme
            selected_crypto.devise = coinDevise
            selected_crypto.apiUrl = apiUrl

            cryptoInfo = requests.get(apiUrl)
            cryptoInfoJson = cryptoInfo.json()
            #print cryptoInfoJson
            selected_crypto.price = cryptoInfoJson['RAW'][coinTrigramme][coinDevise]['PRICE']    
            selected_crypto.openDay = cryptoInfoJson['RAW'][coinTrigramme][coinDevise]['OPENDAY']
            selected_crypto.highDay = cryptoInfoJson['RAW'][coinTrigramme][coinDevise]['HIGHDAY'] 
            selected_crypto.lowDay = cryptoInfoJson['RAW'][coinTrigramme][coinDevise]['LOWDAY']
            selected_crypto.marketCap = cryptoInfoJson['RAW'][coinTrigramme][coinDevise]['MKTCAP'] 
            selected_crypto.evolutionDay = cryptoInfoJson['RAW'][coinTrigramme][coinDevise]['CHANGEPCTDAY']

            return render_template('index.html', selected_crypto=selected_crypto, error=error)
    else:
        return render_template('index.html', error=error)

@app.route('/startbot', methods=['POST','GET'])
def startbot():
    error = None
    return render_template('bot.html', selected_crypto=selected_crypto, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)

#url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=EUR'
#array_eth_price = [] 
#array_eth_buy_price = []
#array_eth_sell_price = []
#timer = 0
#increase_pourcentage = 0.02
#decrease_pourcentage = -0.02
#max_duration = 3600
#
#while True:
#	time.sleep(5)
#	timer += 5
#	r = requests.get(url).json()
#	array_eth_price.append(r[coinDevise])
#	
#	if(len(array_eth_price) > 1):
#		variation_pourcentage = (float(array_eth_price[-1]-array_eth_price[0])/float(array_eth_price[0]))*100
#		
#		if(timer < max_duration and variation_pourcentage > float(increase_pourcentage)):
#			print ("\nHAUSSE DE %.4f\n" % variation_pourcentage)
#			print 'the first price was : ' + str(array_eth_price[0])
#			print 'the last price is : ' + str(array_eth_price[-1])
#			print array_eth_buy_price	
#			array_eth_buy_price.append(array_eth_price[-1])
#			array_eth_sell_price = []
#			array_eth_price = []
#			timer = 0
#	
#		elif(timer < max_duration and variation_pourcentage < float(decrease_pourcentage)):
#			print ("BAISSE DE %.4f\n" % variation_pourcentage)
#			print 'the first price was : ' + str(array_eth_price[0])
#			print 'the last price is : ' + str(array_eth_price[-1])
#			print array_eth_sell_price	
#			array_eth_sell_price.append(array_eth_price[-1])
#			array_eth_buy_price = []
#			array_eth_price = []
#			timer = 0
