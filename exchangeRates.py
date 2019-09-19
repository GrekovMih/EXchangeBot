# вообще черт ногу  сломит Оо из Апи тащить? Из Бд?

import telebot
from telegramApi import bot


def get_exchange_rates(message):
    
    bot.send_message(message.chat.id, ' get_exchange_rates ')



    keyboardInformations = telebot.types.ReplyKeyboardMarkup()
    keyboardInformations.row('/All', '/Key') # О нас   Поддержка