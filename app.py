#!/usr/bin/python
import requests
import json
import time
import sys
from flask_login import LoginManager
from flask import Flask, render_template, request, url_for, redirect, jsonify

#Import class from classes folder
sys.path.insert(0, 'classes')
from coin import Coin
from db import Database
from user import User

app = Flask(__name__)

#Load flask login Class
#login_manager = LoginManager()
#load app inside flask login
#login_manager.init_app(app)

mongo = Database()
selected_crypto = Coin()
base_crypto = [[{'name': 'Bitcoin', 'trigramme': 'BTC'}],[{'name': 'Ethereum', 'trigramme': 'ETH'}],[{'name': 'Litecoin', 'trigramme': 'LTC'}],[{'name': 'Ripple', 'trigramme': 'XRP'}],[{'name': 'EOS', 'trigramme': 'EOS'}]]

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
            
            selected_crypto.price = cryptoInfoJson['RAW'][selected_crypto.trigramme][selected_crypto.devise]['PRICE']    
            selected_crypto.openDay = cryptoInfoJson['RAW'][selected_crypto.trigramme][selected_crypto.devise]['OPENDAY']
            selected_crypto.highDay = cryptoInfoJson['RAW'][selected_crypto.trigramme][selected_crypto.devise]['HIGHDAY'] 
            selected_crypto.lowDay = cryptoInfoJson['RAW'][selected_crypto.trigramme][selected_crypto.devise]['LOWDAY']
            selected_crypto.marketCap = cryptoInfoJson['RAW'][selected_crypto.trigramme][selected_crypto.devise]['MKTCAP'] 
            selected_crypto.evolutionDay = cryptoInfoJson['RAW'][selected_crypto.trigramme][selected_crypto.devise]['CHANGEPCTDAY']

            return render_template('index.html', selected_crypto=selected_crypto, error=error)
    else:
        return render_template('index.html', base_crypto=base_crypto, error=error)

@app.route('/login', methods=['POST','GET'])
def login():
    #form = request.form['loginForm']
    #if form.validate_on_submit():
    #    login_user(user)

    #    flask.flash('Logged in successfully.')

    #    next = flask.request.args.get('next')
    #    if not is_safe_url(next):
    #        return flask.abort(400)

    #    return flask.redirect(next or flask.url_for('index'))
    error = None
    if request.method == 'POST':
        if request.form['validate'] == 'Create Account':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            cryptobot_user = User(username, password, email)
            print username
            print email
            print password
            mongo.create_user(cryptobot_user)
            return render_template('login.html', error=error)
    else:
        return render_template('login.html', error=error)

@app.route('/startbot', methods=['POST','GET'])
def startbot():
    error = None
    selected_crypto.name = request.form['cryptoName']
    selected_crypto.trigramme = request.form['cryptoTrigramme']
    selected_crypto.devise = request.form['cryptoDevise']
    selected_crypto.assign_symbol()
    selected_crypto.url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + selected_crypto.trigramme + '&tsyms=' + selected_crypto.devise
    return render_template('bot.html', selected_crypto=selected_crypto, error=error)


@app.route('/_checkPrice', methods=['GET','POST'])
def checkPrice():
    error=None
    #Receive form and check if it was correctly fill in (with INT) 
    if request.method == 'POST': 
        try:
            check_duration = selected_crypto.check_duration(int(request.form['duration']))
            #If duration is a perso str render an error message to  the user
            if type(check_duration) == str:
                return render_template('bot.html', notInt=check_duration, selected_crypto=selected_crypto, error=error)
            else:
                selected_crypto.duration = check_duration
                selected_crypto.pourcentageHigh = int(request.form['pourcentageUp'])
                selected_crypto.pourcentageLow = int(request.form['pourcentageDown'])
                return render_template('checkPrice.html', selected_crypto=selected_crypto, error=error)
        except ValueError:
            notInt = 'Please you have to enter only numeric values [0-9]'
            return render_template('bot.html', notInt=notInt, selected_crypto=selected_crypto, error=error)
    #Actualize bot GET request
    else:
        selected_crypto.price = selected_crypto.updatedPrice
        new_price = selected_crypto.update_price(selected_crypto.url, selected_crypto.trigramme, selected_crypto.devise)
        selected_crypto.comparePrice.append(new_price)
        if(len(selected_crypto.comparePrice) > 1):
            variation = selected_crypto.price_variation(selected_crypto.comparePrice)

        return jsonify(new_price=new_price, previousPrice=selected_crypto.price, comparePrice=selected_crypto.comparePrice, variation=variation)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
