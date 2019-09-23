# Тащим из БД нужную инфу
import telebot


import psycopg2
from telegramApi import bot

def get_informations(message):

    bot.send_message(message.chat.id, ' Информация ')


    keyboardInformations = telebot.types.ReplyKeyboardMarkup()
    keyboardInformations.row('/All', '/Key') # О нас   Поддержка

    keyboardMain = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # keyboardMain.row('/All', '/Key') #Произвести обмен, мои обмены, настройки, ифнормация
    keyboardMain.row('О нас')  # некошерные команды, а просто текст. Но с красивой клавой можно только так
    keyboardMain.row('Поддержка')













