import balance
import lend
import rate
import record
import settled
import unsettled

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

@bot.message_handler(commands=['rate'], isAdmin=True)
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
def welcome(message):
    sent_msg = bot.send_message(message.chat.id, "Enter Size:")
    bot.register_next_step_handler(sent_msg, size_handler)

def size_handler(message):
    size = message.text
    sent_msg = bot.send_message(message.chat.id, "Enter Rate:")
    bot.register_next_step_handler(sent_msg, rate_handler, size)

def rate_handler(message, size):
	rate = message.text
	sent_msg = bot.send_message(message.chat.id, f"{size} Eth, for {rate} a day. yes/no") 
	bot.register_next_step_handler(sent_msg, placeOrder, size, rate)

def placeOrder(message, size,rate):
	answer = message.text
	if answer == 'yes':
		bot.reply_to(message, lend.PlaceEthLendOrder(size,rate))
	else:
		bot.reply_to(message, 'Canceled')


@bot.message_handler(commands=['balance'], isAdmin= True)
def echo_all(message):
	bot.reply_to(message, balance.getBalance())

bot.add_custom_filter(IsAdmin())

bot.infinity_polling()
