#купи продай и тд

import psycopg2
from qiwi_api import send_p2p
from telegram_api import bot
from sqlalchemy import create_engine
#from db.bot_deal import BotDeal
from sqlalchemy.orm import sessionmaker
from db.crypto_sale import CryptoSale
from db.user_bot_info import UserBotInfo
from db.settings_db import *
from sqlalchemy import update
from glob_stat import *
from reddis_settings import *

from db.bot_deal import BotDeals


# выводятся все варианты продажи крипты, в каждом сообщении будет кликабельная "ссылка" для покупки ее
def to_exchange_coin(message):

    bot.send_message(message.chat.id, ' Обмен валюты ')

    for  id, countcoins, price, text, telephone in session.query(CryptoSale.id, CryptoSale.countcoins, CryptoSale.price,
                                                                    CryptoSale.text, CryptoSale.telephone):
        print("nothing")
        print(countcoins, price, text, telephone )

        command = "/Buy" + str(id)
        bot.send_message(message.chat.id,
                         " В количеcтве " + str(countcoins) + " по цене за монету " + str(price) + " Монета -" + str(
                             text) + " Номер для покупки:  " + str(telephone) + " " + command,
                         )


   #Событие после нажатия на ссылку для покупки, будет задан вопрос сколько шейкелей он хочет
#@bot.message_handler(regexp='^\/(Buy)[0-9]')
def choice_crypto_sale(message):
        global dict_with_state

        #  global numberforBuy

       # numberforBuy = message.text.replace("/Buy", "")

        bot.send_message(message.chat.id, 'Введите количество монет')
        # bot.register_next_step_handler(message, numberforBuy, get_number)

      #  bot.register_next_step_handler(message, lambda msg: request_to_qiwi(numberforBuy, msg))

        dict_with_state[message.from_user.id] = message.text

        conn.hmset("pythonDict", dict_with_state) #redis


#Добавить выбор платежной системы для покупки, qiwi в отдельный модуль и другие систмеы платежные(уточнить какие)  (вывод в кклаве будет, наверное)


    #Пользователь вводит сколько денех он хочет



#@bot.message_handler(content_types=['text']) #уйдет в отдельный модуль
def request_to_qiwi(message):
        print("qiwi qiwi to me")
        global dict_with_state

        id_deal = dict_with_state[message.from_user.id].replace("/Buy", "")
        for id, countcoins, price, text, telephone in session.query(CryptoSale.id, CryptoSale.countcoins, CryptoSale.price,
                                                                CryptoSale.text, CryptoSale.telephone,
                                                                ).filter(CryptoSale.id == str(id_deal)):
            print("nothing")
        print(countcoins, price, text, telephone)
        countCoinAvailable = countcoins

        for keyqiwi, id_telegram in session.query(UserBotInfo.keyqiwi, UserBotInfo.id_telegram,

                                                                ).filter(UserBotInfo.id_telegram==str(message.from_user.id)):
            print("nothing")
        print(keyqiwi, id_telegram)
        api_access_token = keyqiwi

        countCoin = message.text

        #------бронькаем нужное количество монеточек--------

        #может быть фейл, тип во время работы ребутнется и не вернется обратно заброненное, но такая хуйня может быть в любой момент как бы и всегда будет плохо

        print("broniruyu motrherfucke")
        '''
        update_info_bot = session.query(CryptoSale).filter(CryptoSale.id == int(id_deal)).first()
        update_info_bot.countcoins = int(countCoinAvailable) - int(countCoin)
        session.commit()

        result = db.session.query(User.money).with_for_update().filter_by(id=userid).first()
        money = result[0]
        user.money = money - 0.1
        '''



        update_info_bot = session.query(CryptoSale).with_for_update(of=CryptoSale).filter(CryptoSale.id == int(id_deal)).first()
        update_info_bot.countcoins = int(countCoinAvailable) - int(countCoin)
        session.commit()




        # ---------------------------------------------------

        status =''
        if (int(countCoin) <= int(countCoinAvailable)):  # проверить число ли
            print("Отлично! Работаем дальше!")

            sum_p2p = int(countCoin) * int(price)
            print(" sum_p2p " + str(sum_p2p))
           # status = send_p2p('', api_access_token, telephone, 'coin', sum_p2p, message) qiwi qiwi to me
            status = 'ok'
            print(" status " + str(status))

            # ok или трабл
            if (status == 'ok'):

                print("status - OK")
                # добавление произведенной сделки

                newDeal = BotDeals(int(countCoin), int(sum_p2p), str(telephone), str(id_telegram), str(text))
                #newDeal = BotDeals(44, 988, 'din don din', 424, '(text)')

                session.add(newDeal)
                session.commit()



                bot.send_message(message.chat.id, 'Деньги были переведены на счет продавца')
            else:
                bot.send_message(message.chat.id, 'Qiwi failed')
        else:
            print("all wrong")
            bot.send_message(message.chat.id, 'All failed')

        if (status != 'ok'):

            update_info_bot = session.query(CryptoSale).with_for_update(of=CryptoSale).filter(CryptoSale.id == int(id_deal)).first()
            update_info_bot.countcoins = update_info_bot.countcoins + int(countCoin)
            session.commit()




        dict_with_state[message.from_user.id] = ''
        conn.hmset("pythonDict", dict_with_state)  # redis
