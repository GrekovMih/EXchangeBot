# Запрос из БД - botdeal - выводим все по айди пользователя тележки

import psycopg2
from telegramApi import bot
from sqlalchemy import create_engine
from db.botDeal import BotDeals
from db.settings import *

from sqlalchemy.orm import sessionmaker


print("working")

'''
result_set = db.execute("SELECT * FROM botdeals")
for r in result_set:
    print(r)

'''
# bot.send_message(message.chat.id, result_set, )

for count_coins, sum_deal, telephone, id_telegram in session.query(BotDeals.count_coins, BotDeals.sum_deal,
                                                                      BotDeals.telephone, BotDeals.id_telegram,
                                                                      ):
    print("nothing")
    print(count_coins, sum_deal, telephone, id_telegram)

'''
#переделаю я коннекты, переделаю
try:
    connection = psycopg2.connect(user="postgres",
                                  password="45091847",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="cracc")
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT * FROM public.botdeal;"
    cursor.execute(postgreSQL_select_Query)
    mobile_records = cursor.fetchall()

    print("Произведенные операции")
    for row in mobile_records:
        print("Id = ", row[0],)
        print("count_coins = ", row[1])
        print("sum_deal  = ", row[2], "\n")
        print("telephone  = ", row[3], "\n")
        print("id_telegram  = ", row[4], "\n")
        print("text  = ", row[5], "\n")
        command = '/Buy' + str(row[0])
        b = command.split()
        b = ''.join(b)

        bot.send_message(message.chat.id, str(row[4]) + " Купили " + str(row[5]) + " в количеcтве " + str(
            row[1]) + " за  " + str(row[2]) + " рублей  " +  " у  " + str(row[3]) + b,
                         )


except (Exception, psycopg2.Error) as error:
    print ("Error while fetching data from PostgreSQL", error)
finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

'''
