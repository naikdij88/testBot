import telebot
from constants import Data 
import requests
from post import url_send 
from urllib.parse import quote_plus
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s'
)

def main():
    bot = telebot.TeleBot(Data.token)

    @bot.message_handler(content_types=['text'])
    def send_welcome(message):
        if message.text != ' ':
            #bot.send_message(chat_id=, text="b")
            msg_send(message.text)
            

        elif message.text == 'b':
            bot.reply_to(message, "a")
    

    bot.polling(none_stop=True, interval=0)

def msg_send(msg):
    result = quote_plus(msg)
    r = requests.post(url_refresh(), data=result)
        
def url_refresh():
    url = url_send()
    logging.debug('новый :' + url)
    return url

url = url_refresh()

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
            exit()