#КНопочки главного меню

import telegramApi


keyboardMain = telebot.types.ReplyKeyboardMarkup()
#keyboardMain.row('/All', '/Key') #Произвести обмен, мои обмены, настройки, ифнормация
keyboardMain.row('Произвести обмен', 'мои обмены','моя борьба','моя оборона',  'настройки','информация','Курсы обмена' ) #некошерные команды, а просто текст. Но с красивой клавой можно только так





bot.polling()
