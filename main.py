#КНопочки главного меню
import telebot
from telegramApi import bot
from historyOfExchanges import history_of_exchanges
from informations import get_informations
from exchangeRates import get_exchange_rates
from settings import change_settings
from toExchangeCoin import to_exchange_coin



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в телеграм бот cracc', reply_markup=keyboardMain)
    bot.send_message(message.chat.id, ' working ')


keyboardMain = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#keyboardMain.row('/All', '/Key') #Произвести обмен, мои обмены, настройки, ифнормация
keyboardMain.row('Произвести обмен') #некошерные команды, а просто текст. Но с красивой клавой можно только так
keyboardMain.row('Мои обмены')
keyboardMain.row('Настройки')
keyboardMain.row('Информация')
keyboardMain.row('Курсы обмена')

# allTextCommand обработка всех текстовых команд


@bot.message_handler(content_types=['text'])
def send_text(message):
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




bot.polling()
