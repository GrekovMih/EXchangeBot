import telebot

def change_settings(message):
    keyboardSettings = telebot.types.ReplyKeyboardMarkup()
    keyboardSettings.row('/All', '/Key') #Ввести ключ киви, еще какой-нибудь ключ и тд
