import telebot
from telegramApi import bot


def change_settings(message):
    bot.send_message(message.chat.id, ' change_settings ')

    keyboardSettings = telebot.types.ReplyKeyboardMarkup()
    keyboardSettings.row('/All', '/Key') #Ввести ключ киви, еще какой-нибудь ключ и тд
