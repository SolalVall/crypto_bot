#!/usr/bin/python
import requests
import json
import time
from coin import Coin
from flask import Flask, render_template, request, url_for, redirect, jsonify

app = Flask(__name__)
selected_crypto = Coin()

@app.route('/', methods=['POST','GET'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['bttnInfo'] == 'Get Info':
            selected_crypto.trigramme = request.form['cryptoTrigramme']
            selected_crypto.devise = request.form['cryptoDevise'] 
            selected_crypto.assign_symbol()
            selected_crypto.url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + selected_crypto.trigramme + '&tsyms=' + selected_crypto.devise
            
            cryptoInfo = requests.get(selected_crypto.url)
            cryptoInfoJson = cryptoInfo.json()
            #print cryptoInfoJson
            
            selected_crypto.price = cryptoInfoJson['RAW'][selected_crypto.trigramme][selected_crypto.devise]['PRICE']    
            selected_crypto.openDay = cryptoInfoJson['RAW'][selected_crypto.trigramme][selected_crypto.devise]['OPENDAY']
            selected_crypto.highDay = cryptoInfoJson['RAW'][selected_crypto.trigramme][selected_crypto.devise]['HIGHDAY'] 
            selected_crypto.lowDay = cryptoInfoJson['RAW'][selected_crypto.trigramme][selected_crypto.devise]['LOWDAY']
            selected_crypto.marketCap = cryptoInfoJson['RAW'][selected_crypto.trigramme][selected_crypto.devise]['MKTCAP'] 
            selected_crypto.evolutionDay = cryptoInfoJson['RAW'][selected_crypto.trigramme][selected_crypto.devise]['CHANGEPCTDAY']

            return render_template('index.html', selected_crypto=selected_crypto, error=error)
    else:
        return render_template('index.html', error=error)

@app.route('/startbot', methods=['POST','GET'])
def startbot():
    error = None
    if request.method == "POST":
        #Check if HTML inputs are INT or STRING whit int()
        try:
            selected_crypto.duration = int(request.form['duration'])
            selected_crypto.pourcentageHigh = int(request.form['pourcentageUp'])
            selected_crypto.pourcentageLow = int(request.form['pourcentageDown'])
            return render_template('checkPrice.html', selected_crypto=selected_crypto, error=error)
        except ValueError:
            notInt = 'Please you have to enter only numeric values [0-9]'
            return render_template('bot.html', notInt=notInt, selected_crypto=selected_crypto, error=error)
    else:
        return render_template('bot.html', selected_crypto=selected_crypto, error=error)


@app.route('/_checkPrice', methods=['GET'])
def checkPrice():
    result = selected_crypto.checkPrice(selected_crypto.url, selected_crypto.trigramme
    , selected_crypto.devise, selected_crypto.price)
    print result 
    return jsonify(result=result)

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
#	array_eth_price.append(r[selected_crypto.devise])
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
