import telebot


#set your variables
API_KEY = ("Your API")          
bot = telebot.TeleBot(API_KEY)   


#First reply message
@bot.message_handler(commands=['hi'])
def hi(message):
  bot.reply_to(message, "Hall")

  
#second message
@bot.message_handler(commands=['ping'])
def Ping(message):
  bot.send_message(message.chat.id, 'Pong')

  
#starts the bot
bot.polling()
