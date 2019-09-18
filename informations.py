# Тащим из БД нужную инфу
import telebot


import psycopg2
from telegramApi import bot

def get_informations(message):



    keyboardInformations = telebot.types.ReplyKeyboardMarkup()
    keyboardInformations.row('/All', '/Key') # О нас   Поддержка



