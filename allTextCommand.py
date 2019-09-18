#команды что не вложенны будут, другое  можно будет вкладывать и перехватывать по  другому

import telegramApi
import main



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Произвести обмен':
        to_exchange_coin
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')