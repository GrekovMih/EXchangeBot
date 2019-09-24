# вообще черт ногу  сломит Оо из Апи тащить? Из Бд?

import telebot
from telegram_api import bot


def get_exchange_rates(message):
    
    bot.send_message(message.chat.id, 'Курсы обмена:   ')
