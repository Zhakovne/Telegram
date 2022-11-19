import telebot

bot = telebot.TeleBot('5742880011:AAH8MkhWZox0v3j7o9nggEhKWHctUvWDhGU')
print('Бот запущен!')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()



