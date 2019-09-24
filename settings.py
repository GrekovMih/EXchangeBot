import telebot
from telegram_api import bot

import psycopg2
from qiwi_api import send_p2p
from telegram_api import bot
from sqlalchemy import create_engine
#from db.bot_deal import BotDeal
from sqlalchemy.orm import sessionmaker
from db.crypto_sale import CryptoSale
from db.user_bot_info import UserBotInfo
from db.settings import *
from sqlalchemy import update
from db.settings import *


dict_with_state = {}




def change_settings(message):
    global dict_with_state

    bot.send_message(message.chat.id, ' change_settings ')

    keyboardSettings = telebot.types.ReplyKeyboardMarkup()

    # keyboardMain.row('/All', '/Key') #Произвести обмен, мои обмены, настройки, ифнормация
    keyboardSettings.row('Ввести ключ API от QIWI')  # некошерные команды, а просто текст. Но с красивой клавой можно только так
    keyboardSettings.row('Мои адреса')
    keyboardSettings.row('Уведомления')



    bot.send_message(message.chat.id, ' Settings ', reply_markup=keyboardSettings)

    dict_with_state[message.from_user.id] = 'settings'


def change_settings_command(message):
    global dict_with_state
    if message.text == 'Ввести ключ API от QIWI':
       bot.send_message(message.chat.id, ' Введите  ваш  ключ API от QIWI ')
       dict_with_state[message.from_user.id] = 'settings_api_qiwi'


    elif message.text == 'Настройки':
        bot.send_message(message.chat.id, ' !Настройки ')
    elif message.text == 'Информация':
        bot.send_message(message.chat.id, ' Информация! ')




def change_settings_qiwi_api(message):

    print("hop hop")

    bot.send_message(message.chat.id, ' Write in db ')

    keyqiwi = message.text # insert or update
    id_telegram = message.from_user.id
    newUserBotInfo = UserBotInfo(keyqiwi, id_telegram)
    session.add(newUserBotInfo)
    session.commit()

