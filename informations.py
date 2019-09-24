# Тащим из БД нужную инфу
import telebot


import psycopg2
from telegram_api import bot

def get_informations(message):


    keyboardInformations = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboardMain.row('/All', '/Key') #Произвести обмен, мои обмены, настройки, ифнормация
    keyboardInformations.row('О нас')  # некошерные команды, а просто текст. Но с красивой клавой можно только так
    keyboardInformations.row('Поддержка')
    keyboardInformations.row('Главное меню')



    bot.send_message(message.chat.id, ' Информация ', reply_markup=keyboardInformations)


    @bot.message_handler(content_types=['text'])

    def send_text(message):
        if message.text == 'О нас':
            bot.send_message(message.chat.id, ' Crocc - это калево ')
        elif message.text == 'Поддержка':
            bot.send_message(message.chat.id, ' Брат за брата ')














