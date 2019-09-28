#Запрос из БД - botdeal - выводим все по айди пользователя тележки

import psycopg2
from telegram_api import bot
from sqlalchemy import create_engine
#from db.bot_deal import BotDeal
from sqlalchemy.orm import sessionmaker
from db.bot_deal import BotDeals
from db.settings_db import *

def history_of_exchanges(message):

    bot.send_message(message.chat.id, ' История операций ')



    for countcoins, sumdeal, telephone, idtelegram in session.query(BotDeals.countcoins, BotDeals.sumdeal,
                                                                    BotDeals.telephone, BotDeals.idtelegram,
                                                                    ).filter(BotDeals.idtelegram==message.from_user.id):
        print("nothing")
        print(countcoins, sumdeal, telephone, idtelegram)
        bot.send_message(message.chat.id, " Купили " + str(countcoins) + " в количеcтве " + str(
            countcoins) + " за  " + str(sumdeal) + " рублей  " + " у  " + str(telephone),
                         )


    '''
    for countcoins, sumdeal, telephone, idtelegram in session.query(BotDeals.countcoins, BotDeals.sumdeal,
                                                                    BotDeals.telephone, BotDeals.idtelegram,
                                                                    ):
        print("nothing")
        print(countcoins, sumdeal, telephone, idtelegram)
        bot.send_message(message.chat.id, str(idtelegram) + " Купили " + str(countcoins) + " в количеcтве " + str(
            countcoins) + " за  " + str(sumdeal) + " рублей  " + " у  " + str(telephone),
                         )
                         
    '''

