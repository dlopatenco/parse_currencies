import telebot
from telebot.types import Message
from changeValletFunc import parseData
from pretyTable import prety_data
changeData = parseData()

TOKEN = '1381922935:AAGQaF29K33oY_oTwvNH0voyzCeMb08QTIU'
bot = telebot.TeleBot(TOKEN)
name = 'Dan'
@bot.message_handler(commands=['start', 'eur','usd','ron', 'rub'])
def send_data(message):
    if message.text == '/start':
        bot.reply_to(message, f'Hello {message.from_user.first_name}!')
        bot.send_photo(chat_id=message.from_user.id, photo=open('data.png', 'rb'))

    elif message.text == '/eur':
        bot.send_message(chat_id=message.from_user.id,text=f'''{changeData[['Denumirea Bancii','Cumparare EUR','Vinzare EUR']]}''')

    elif message.text == '/usd':
        bot.send_message(chat_id=message.from_user.id,text=f'''{changeData[['Denumirea Bancii','Cumparare USD','Vinzare USD']]}''')

    elif message.text == '/ron':
        bot.send_message(chat_id=message.from_user.id,text=f'''{changeData[['Denumirea Bancii','Cumparare RON','Vinzare RON']]}''')

    elif message.text == '/rub':
        bot.send_message(chat_id=message.from_user.id,text=f'''{changeData[['Denumirea Bancii','Cumparare RUB','Vinzare RUB']]}''')


print('Bot started')
bot.polling()

