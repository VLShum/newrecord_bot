import telebot
from hola import greetings
from telebot import TeleBot


TOKEN = '1851842646:AAEgF2SuLZm3iQzNBy-2Mv2M-ZEWuMoZVzs'

bot: TeleBot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	    bot.reply_to(message, "Здравствуйте, рады видеть Вас у нас в салоне")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	for i in greetings:
		if message.text == i:
			bot.reply_to(message, 'Желаете записаться на прием?')
			#bot.reply_to(message, message.text)

bot.polling()