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


keyboardMain = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#keyboardMain.row('/All', '/Key') #Произвести обмен, мои обмены, настройки, ифнормация
keyboardMain.row('Произвести обмен' ) #некошерные команды, а просто текст. Но с красивой клавой можно только так
keyboardMain.row('Мои обмены' )
keyboardMain.row( 'Настройки' )
keyboardMain.row('информация' )
keyboardMain.row('Курсы обмена' )


# allTextCommand обработка всех текстовых команд


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Произвести обмен':
        to_exchange_coin(message)
    elif message.text.lower() == 'Мои обмены':
        history_of_exchanges(message)
    elif message.text.lower() == 'Настройки':
        change_settings(message)
    if message.text.lower() == 'Информация':
        get_informations(message)
    elif message.text.lower() == 'Курсы обмена':
        get_exchange_rates(message)









bot.polling()
