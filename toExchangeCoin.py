#купи продай и тд

import psycopg2
from qiwiApi import send_p2p
from telegramApi import bot
from sqlalchemy import create_engine
#from db.botDeal import BotDeal
from sqlalchemy.orm import sessionmaker
from db.cryptoSale import CryptoSale
from db.userBotInfo import UserBotInfo
from db.settings import *
from sqlalchemy import update


# выводятся все варианты продажи крипты, в каждом сообщении будет кликабельная "ссылка" для покупки ее
def to_exchange_coin(message):

    bot.send_message(message.chat.id, ' Обмен валюты ')

    for id, count_coins, price, text, telephone in session.query(CryptoSale.id, CryptoSale.count_coins, CryptoSale.price,
                                                                    CryptoSale.text, CryptoSale.telephone):
        print("nothing")
        print(count_coins, price, text, telephone )

        bot.send_message(message.chat.id, " В количеcтве " + str(count_coins) + " по цене за монету " + str(price) + "Монета -"+ str(text) +" Номер для покупки:  " + str(telephone) + "  " ,
                 )






   #Событие после нажатия на ссылку для покупки, будет задан вопрос сколько шейкелей он хочет
    @bot.message_handler(regexp='^\/(Buy)[0-9]')
    def start_message(message):
        #  global numberforBuy

        numberforBuy = message.text.replace("/Buy", "")

        bot.send_message(message.chat.id, 'Введите количество монет')
        # bot.register_next_step_handler(message, numberforBuy, get_number)

        bot.register_next_step_handler(message, lambda msg: request_to_qiwi(numberforBuy, msg))


#Добавить выбор платежной системы для покупки, qiwi в отдельный модуль и другие систмеы платежные(уточнить какие)  (вывод в кклаве будет, наверное)


    #Пользователь вводит сколько денех он хочет
    @bot.message_handler(content_types=['text']) #уйдет в отдельный модуль
    def request_to_qiwi(numberforBuy, message):
        #   numberforBuy = message.text

        #  global numberforBuy
        print("numberforBuy")

        print(numberforBuy)

        for keyqiwi, id_telegram in session.query(UserBotInfo.keyqiwi, UserBotInfo.id_telegram,

                                                                ).filter(UserBotInfo.id_telegram==str(message.from_user.id)):
            print("nothing")
            print(keyqiwi, id_telegram)

            api_access_token = api_access_token

        for id, count_coins, price, text, telephone in session.query(CryptoSale.id, CryptoSale.count_coins, CryptoSale.price,
                                                                CryptoSale.text, CryptoSale.telephone,
                                                                ).filter(CryptoSale.id == str(numberforBuy)):
            print("nothing")
            print(count_coins, price, text, telephone)

            bot.send_message(message.chat.id,
                             " В количеcтве " + str(count_coins) + " по цене за монету " + str(price) + "Монета -" + str(
                                 text) + " Номер для покупки:  " + str(telephone) + "  ",
                             )
            countCoinAvailable = count_coins


        countCoin = message.text

        print("countCoin" + countCoin)

        if (int(countCoin) <= int(countCoinAvailable)):  # проверить число ли
            print("Отлично! Работаем дальше!")

            sum_p2p = int(countCoin) * int(price)
            print("sum_p2p" + str(sum_p2p))

            to_qw = telephone

            status = send_p2p('', api_access_token, telephone, '', sum_p2p, message)

            # ok или трабл

            if (status == 'ok'):
                newDeal = BotDeals(count_coins, sum_p2p, telephone, id_telegram, text)
                session.add(newDeal)
                updateDeal = update(BotDeals).where(BotDeals.id == numberforBuy).values(countCoin=countCoinAvailable - countCoin )
                bot.send_message(message.chat.id, 'Деньги были переведены на счет продавца')

        
