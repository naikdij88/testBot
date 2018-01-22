
import telebot
from constants import Data 

def main():
    bot = telebot.TeleBot(Data.token)
    bot.send_message(chat_id="211951342", text="Привет!!!")
    @bot.message_handler(content_types=['text'])
    def send_welcome(message):
        if message.text == 'a':
            bot.reply_to(message, "b")

        elif message.text == 'b':
            bot.reply_to(message, "a")
    

    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
            exit()