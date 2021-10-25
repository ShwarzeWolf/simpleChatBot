#pip install pyTelegramBotAPI

import telebot
from random import randint

token = '' # your token here

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_description(message):
    bot.send_message(message.chat.id, 'Это тестовый бот, который будкет отправлять картинки')


@bot.message_handler(commands=['get'])
def send_photo(message):
    baseUrl = 'https://aws.random.cat/view/'
    number = randint(0, 1000)
    bot.send_photo(message.chat.id, baseUrl + str(number))


bot.polling(none_stop=True, interval=0)

