# КНопочки главного меню
import telebot
from telegram_api import bot
from history_of_exchanges import history_of_exchanges
from informations import get_informations
from exchange_rates import get_exchange_rates
from settings import *
from to_exchange_coin import *


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в телеграм бот cracc', reply_markup=keyboardMain)
    bot.send_message(message.chat.id, ' working ')


keyboardMain = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
# keyboardMain.row('/All', '/Key') #Произвести обмен, мои обмены, настройки, ифнормация
keyboardMain.row('Произвести обмен')  # некошерные команды, а просто текст. Но с красивой клавой можно только так
keyboardMain.row('Мои обмены')
keyboardMain.row('Настройки')
keyboardMain.row('Информация')
keyboardMain.row('Курсы обмена')







#-----------------Обмен-------------
@bot.message_handler(regexp='^\/(Buy)[0-9]')
def call_from_to_exchange_coin(message):
    choice_crypto_sale(message)
#-----------------------------------



# allTextCommand обработка всех текстовых команд


@bot.message_handler(content_types=['text'])
def send_text(message):
 global dict_with_state


 try:
    print (dict_with_state[message.from_user.id])

    #-----------------Настройка-------------
    if dict_with_state[message.from_user.id] == 'settings':  # try
        bot.send_message(message.chat.id, ' olololo ')
        print("settings")
        change_settings_command(message)
    elif dict_with_state[message.from_user.id] == 'settings_api_qiwi':
        print("settings api")
        change_settings_qiwi_api(message)

    #-----------------Обмен-------------

    elif "Buy" in dict_with_state[message.from_user.id]:
        request_to_qiwi(message)
        print("request_to_qiwi")


 except:

    if message.text == 'Произвести обмен':
        to_exchange_coin(message)

    elif message.text == 'Мои обмены':
        bot.send_message(message.chat.id, ' Мои обмены ')
        history_of_exchanges(message)
    elif message.text == 'Настройки':
        change_settings(message)
    if message.text == 'Информация':
        bot.send_message(message.chat.id, ' Информация ')
        get_informations(message)

    elif message.text == 'Курсы обмена':
        get_exchange_rates(message)


# вообще хз


#

bot.polling()
