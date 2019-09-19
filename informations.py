# Тащим из БД нужную инфу
import telebot


import psycopg2
from telegramApi import bot

def get_informations(message):

    bot.send_message(message.chat.id, ' get_informations ')


    keyboardInformations = telebot.types.ReplyKeyboardMarkup()
    keyboardInformations.row('/All', '/Key') # О нас   Поддержка



