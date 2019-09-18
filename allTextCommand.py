#команды что не вложенны будут, другое  можно будет вкладывать и перехватывать по  другому

from telegramApi import bot 
from historyOfExchanges import history_of_exchanges
from informations import get_informations
from exchangeRates import get_exchange_rates
from settings import change_settings
from toExchangeCoin import to_exchange_coin



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Произвести обмен':
        to_exchange_coin
    elif message.text.lower() == 'Мои обмены':
        history_of_exchanges
    elif message.text.lower() == 'Настройки':
        change_settings
    if message.text.lower() == 'Информация':
        get_informations
    elif message.text.lower() == 'Курсы обмена':
        get_exchange_rates
