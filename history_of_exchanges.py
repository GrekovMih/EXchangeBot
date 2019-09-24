#Запрос из БД - botdeal - выводим все по айди пользователя тележки

import psycopg2
from telegram_api import bot
from sqlalchemy import create_engine
#from db.bot_deal import BotDeal
from sqlalchemy.orm import sessionmaker
from db.bot_deal import BotDeals
from db.settings import *

def history_of_exchanges(message):

    bot.send_message(message.chat.id, ' История операций ')

    for count_coins, sum_deal, telephone, id_telegram in session.query(BotDeals.count_coins, BotDeals.sum_deal,
                                                                    BotDeals.telephone, BotDeals.id_telegram,
                                                                    ):
        print("nothing")
        print(count_coins, sum_deal, telephone, id_telegram)
        bot.send_message(message.chat.id, str(id_telegram) + " Купили " + str(count_coins) + " в количеcтве " + str(
            count_coins) + " за  " + str(sum_deal) + " рублей  " + " у  " + str(telephone),
                         )

