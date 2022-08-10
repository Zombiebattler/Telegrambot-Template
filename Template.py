import telebot

API_KEY = ("your api key")
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['ping'])
def Ping(message):
  bot.send_message(message.chat.id, 'Pong')
  
bot.polling()
