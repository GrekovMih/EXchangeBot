#КНопочки главного меню
import telebot
from telegramApi import bot


keyboardMain = telebot.types.ReplyKeyboardMarkup()
#keyboardMain.row('/All', '/Key') #Произвести обмен, мои обмены, настройки, ифнормация
keyboardMain.row('Произвести обмен', 'Мои обмены','моя борьба','моя оборона',  'Настройки','Информация','Курсы обмена' ) #некошерные команды, а просто текст. Но с красивой клавой можно только так
# allTextCommand обработка всех текстовых команд




bot.polling()
