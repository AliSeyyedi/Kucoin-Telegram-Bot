from kucoin.client import Client
from kucoin.market import market
from kucoin.asyncio import KucoinSocketManager
from webbrowser import get
import requests
import json
import time
import pybase64 as base64
import hmac
import hashlib
from datetime import datetime
import pytz

import balance
import lend
import rate
import record
import settled
import unsettled

# client = Client(api_key, api_secret, api_passphrase)

# real acc
# api_key = '6331daf3b72af700018adee2'
# api_secret = '020c7d27-158c-4cec-bc9e-6ff0b03ea848'
# api_passphrase = 'newLending'
# url = 'https://api.kucoin.com'

# test acc
api_key = '6336c39529c69200011ee3e3'
api_secret = '5e74c38d-4623-417e-9b38-517d2909a462'
api_passphrase = 'sandbox'
url = 'https://openapi-sandbox.kucoin.com'

import telebot
bot = telebot.TeleBot("5770954393:AAGNoG-90wKV-Xwpaei-PKGn-QwAyljolok")

class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    key='isAdmin'
    @staticmethod
    def check(message: telebot.types.Message):
        return message.chat.username in ['AliSeyyedi','Millad_Ghodrati']

@bot.message_handler(commands=['start'], isAdmin= True)
def echo_all(message):
	bot.reply_to(message, 'Welcome '+ str(message.chat.first_name))

@bot.message_handler(commands=['ethrate'], isAdmin=True)
def echo_all(message):
	bot.reply_to(message, rate.getEthRate())

@bot.message_handler(commands=['unsettled'], isAdmin=True)
def echo_all(message):
	bot.reply_to(message, unsettled.getUnsettledOrders())

@bot.message_handler(commands=['settled'], isAdmin=True)
def echo_all(message):
	bot.reply_to(message, settled.getSettledOrders())

@bot.message_handler(commands=['record'], isAdmin=True)
def echo_all(message):
	bot.reply_to(message, record.getRecord())

@bot.message_handler(commands=['lend'], isAdmin= True)
def echo_all(message):
	bot.reply_to(message, lend.PlaceEthLendOrder())

@bot.message_handler(commands=['balance'], isAdmin= True)
def echo_all(message):
	bot.reply_to(message, balance.getBalance())

bot.add_custom_filter(IsAdmin())

bot.infinity_polling()
