import telebot
from constants import Data 
import requests
import post
from urllib.parse import quote_plus

def main():
    bot = telebot.TeleBot(Data.token)

    @bot.message_handler(content_types=['text'])
    def send_welcome(message):
        if message.text != ' ':
            #bot.send_message(chat_id=, text="b")
            bot1(message.text)
            

        elif message.text == 'b':
            bot.reply_to(message, "a")
    

    bot.polling(none_stop=True, interval=0)

def bot1(msg):
    result = quote_plus(msg)
    requests.post(post.url, data=result)


if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
            exit()