# вообще черт ногу  сломит Оо из Апи тащить? Из Бд?

import telebot


import psycopg2
from telegramApi import bot

def get_exchange_rates(message):



    keyboardInformations = telebot.types.ReplyKeyboardMarkup()
    keyboardInformations.row('/All', '/Key') # О нас   Поддержка