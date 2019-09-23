#купи продай и тд

import psycopg2
from qiwiApi import send_p2p
from telegramApi import bot



# выводятся все варианты продажи крипты, в каждом сообщении будет кликабельная "ссылка" для покупки ее
def to_exchange_coin(message):

    bot.send_message(message.chat.id, ' to_exchange_coin ')


    #переделаю я коннекты, переделаю
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="45091847",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="cracc")
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT * FROM public.cryptosale;"
        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        print("Предложения по продаже крипты")
        for row in mobile_records:
            print("Id = ", row[0],)
            print("countcoins = ", row[1])
            print("price  = ", row[2], "\n")
            print("nameCoins  = ", row[3], "\n")
            print("number  = ", row[4], "\n")
            command = '/Buy' + str(row[0])
            b = command.split()
            b = ''.join(b)

            bot.send_message(message.chat.id, " username продает " + str(row[3]) + " в количеcтве " + str(
                row[1]) + " по цене за монету " + str(row[2]) + " Номер для покупки:  " + row[4] + "  " + b,
                             )


    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")






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

        try:
            connection = psycopg2.connect(user="postgres",
                                          password="45091847",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="cracc")
            cursor = connection.cursor()
            postgreSQL_select_Query = "SELECT * FROM public.userbotinfo where public.userbotinfo.idtelegram = '" + str(
                message.from_user.id) + "';"
            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()

            for row in mobile_records:
                api_access_token = row[0]
            #   print("api_access_token" + api_access_token)

            cursor = connection.cursor()
            postgreSQL_select_Query = "SELECT * FROM public.cryptosale where public.cryptosale.id = '" + str(
                numberforBuy) + "';"
            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()

            for row in mobile_records:
                countCoinAvailable = row[1]
                price = row[2]
                telephone = row[3]
            #   print("countCoinAvailable" + countCoinAvailable)
            #  print("price" + price)


        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

        # to_qw = numberforBuy

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
                con = psycopg2.connect(
                    user="postgres",
                    password="45091847",
                    host="127.0.0.1",
                    port="5432",
                    database="cracc"
                )

                print("Database opened successfully")
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO  botdeal VALUES  ('" + str(countCoin) + "', '"
                    + str(sum_p2p) + to_qw + str(message.from_user.id) + "');"
                )

                con.commit()
                print("Record inserted successfully")

                con.close()


    ''' 
    уменьшать в таблице доступные монетки
                cur = con.cursor()
                cur.execute(
                    "UPDATE  botdeal VALUES  ('" + str(countCoin) + "', '"
                    + str(sum_p2p) + to_qw + str(message.from_user.id) + "');"
                )

                con.commit()
                print("Record inserted successfully")

    '''


    bot.send_message(message.chat.id, 'Деньги были переведены на счет продавца')

        
