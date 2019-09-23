# Тащим из БД нужную инфу
import telebot


import psycopg2
from telegramApi import bot

def get_informations(message):

    bot.send_message(message.chat.id, ' get_informations ')


    keyboardInformations = telebot.types.ReplyKeyboardMarkup()
    keyboardInformations.row('/All', '/Key') # О нас   Поддержка

    get_informations_second(message)


def get_informations_second(message):
    bot.send_message(message.chat.id, 'kek')
    get_informations_second(message)
    @bot.message_handler(content_types=['text'])  # уйдет в отдельный модуль
    def request_to_qiwi(numberforBuy, message):
        bot.send_message(message.chat.id, ' only you ')








