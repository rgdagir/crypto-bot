# CryptoBot v2.0
# Author: rgdagir (www.github.com/rgdagir)

#importing useful libs
import requests
import re
import json

# fetch_notifs will work with the open browser, after the user
# was logged into Facebook, and fetch all NEW (aka unread) 
# notifications for the user. This function does not mark the 
# fetched notifications as read, though

def fetch_buy_price(crypto, target_currency = "USD"):
    if crypto == "bitcoin": # imporve parsing
        crypto = "BTC"
    elif crypto == "ethereum":
        crypto = "ETH"
    # why I'm not using coinbase specific libs, client module? because, even though it would save me some lines of code, I would need to upload my API key and API secret up in the cloud.
    get_url = "https://api.coinbase.com/v2/prices/" + crypto + "-" + target_currency + "/buy"
    price_data = requests.get(get_url)
    print(price_data)
    price = price_data.json()
    print(price)
    price = price["data"]["amount"]
    return (crypto + " to "+ target_currency+ " Coinbase buy price: "+ str(price))

# This fucntion sends the notifications to the user on Telegram,
# using the string with all notifications and the Telegram token
# to make a POST on the Telegram's API

def send_message_telegram(content, token, chat_id):
    # sending telegram message 
    method = "sendMessage"
    post_url = "https://api.telegram.org/bot" + token + "/" + method
    # setting params as dicts
    data = { 
        "chat_id":chat_id,
        "text":content
    }
    headers = {
        "Content-Type":"application/json"    
    }
    # calling the API
    send_message = requests.post(post_url, data=json.dumps(data), headers=headers)

