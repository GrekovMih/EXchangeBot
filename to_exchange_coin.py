#купи продай и тд

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


dict_with_state = {}



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

        numberforBuy = message.text.replace("/Buy", "")

        bot.send_message(message.chat.id, 'Введите количество монет')
        # bot.register_next_step_handler(message, numberforBuy, get_number)

      #  bot.register_next_step_handler(message, lambda msg: request_to_qiwi(numberforBuy, msg))

        dict_with_state[message.from_user.id] = numberforBuy


#Добавить выбор платежной системы для покупки, qiwi в отдельный модуль и другие систмеы платежные(уточнить какие)  (вывод в кклаве будет, наверное)


    #Пользователь вводит сколько денех он хочет



@bot.message_handler(content_types=['text']) #уйдет в отдельный модуль
def request_to_qiwi(message):
        global dict_with_state
              
        id_deal = dict_with_state[message.from_user.id].replace("/Buy", "")



        for keyqiwi, id_telegram in session.query(UserBotInfo.keyqiwi, UserBotInfo.id_telegram,

                                                                ).filter(UserBotInfo.id_telegram==str(message.from_user.id)):
            print("nothing")
            print(keyqiwi, id_telegram)

            api_access_token = api_access_token

        for id, countcoins, price, text, telephone in session.query(CryptoSale.id, CryptoSale.countcoins, CryptoSale.price,
                                                                CryptoSale.text, CryptoSale.telephone,
                                                                ).filter(CryptoSale.id == str(id_deal)):
            print("nothing")
            print(count_coins, price, text, telephone)

            bot.send_message(message.chat.id,
                             " В количеcтве " + str(countcoins) + " по цене за монету " + str(price) + " Монета -" + str(
                                 text) + " Номер для покупки:  " + str(telephone) + " " ,
                             )
            countCoinAvailable = countcoins

        countCoin = message.text

        print("countCoin" + countCoin)

        if (int(countCoin) <= int(countCoinAvailable)):  # проверить число ли
            print("Отлично! Работаем дальше!")

            sum_p2p = int(countCoin) * int(price)
            print("sum_p2p" + str(sum_p2p))

            status = send_p2p('', api_access_token, telephone, '', sum_p2p, message)

            # ok или трабл

            if (status == 'ok'):
                newDeal = BotDeals(count_coins, sum_p2p, telephone, id_telegram, text)
                session.add(newDeal)
                updateDeal = update(BotDeals).where(BotDeals.id == numberforBuy).values(countCoin=countCoinAvailable - countCoin )
                bot.send_message(message.chat.id, 'Деньги были переведены на счет продавца')
