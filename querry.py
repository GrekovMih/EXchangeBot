# Запрос из БД - botdeal - выводим все по айди пользователя тележки

import psycopg2
from telegram_api import bot
from sqlalchemy import create_engine
from db.bot_deal import BotDeals
from db.settings_db import *
from db.crypto_sale import CryptoSale



from db.user_bot_info import UserBotInfo

from sqlalchemy import update


from sqlalchemy.orm import sessionmaker


print("working")

'''
result_set = db.execute("SELECT * FROM botdeals")
for r in result_set:
    print(r)

'''
# bot.send_message(message.chat.id, result_set, )
def ololo():
    keyqiwi = '1488' # insert or update
    id_telegram = 'message.from_user.id'

    '''
    update_info_bot = session.query(UserBotInfo).filter(UserBotInfo.id_telegram == id_telegram).first()
    update_info_bot.keyqiwi = keyqiwi
    session.commit()
    '''

'''
    newUserBotInfo = UserBotInfo(14, 88)
    session.add(newUserBotInfo)
    session.commit()
    print("insert")
'''


#ololo()

'''
newDeal = BotDeals(14, 88, 'din din', 42, '(text)')
session.add(newDeal)
session.commit()
'''

update_info_bot = session.query(UserBotInfo).with_for_update(of=UserBotInfo).filter(UserBotInfo.id_telegram == '14').first()
update_info_bot.keyqiwi = '99'
session.commit()

'''
try:
    update_info_bot = session.query(UserBotInfo).filter(UserBotInfo.id_telegram == '14').first()
    update_info_bot.keyqiwi = '99'
    session.commit()
    print("update")

except:

    try:
        newUserBotInfo = UserBotInfo('message.text', '14')
        session.add(newUserBotInfo)
        session.commit()
        print("insert")

    except:

        print("failed db")

'''

'''
newUserBotInfo = UserBotInfo(1, 88)
session.add(newUserBotInfo)
session.commit()
print("insert")


newUserBotInfo = UserBotInfo(4, 88)
session.add(newUserBotInfo)
session.commit()
print("insert")


newUserBotInfo = UserBotInfo(8, 88)
session.add(newUserBotInfo)
session.commit()
print("insert")

newUserBotInfo = UserBotInfo(1, 88)
session.add(newUserBotInfo)
session.commit()
print("insert")
'''

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
