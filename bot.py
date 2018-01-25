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
        if message.text == '/help' or message.text == '/help@MySecondLife_bot':
            help_text = '''     
            /online_list - Возвращает список Аватаров находящихся в данный момент Онлайн, из списка '~friends'. 
            /online_list_on - Включает автоматическое оповещение активности авторов из списка при изменении статуса (Online-Offline).
            /online_list_off - Выключает автоматическое оповещение активности авторов из списка.
            /guest_list - Выводит список Аватаров приближавшихся к объекту на указанный радиус (не более 96м).
            /guest_list_on - Включает автоматическое оповещение при нахождении Аватара в указанном радиусе.
            /guest_list_off - Выключает автоматическое оповещение.
            '''
            bot.reply_to(message, help_text)

        elif message.text == '/online_list' or message.text == '/online_list@MySecondLife_bot':
                msg_send('_1')

        elif message.text == '/online_list_on' or message.text == '/online_list_on@MySecondLife_bot':
                msg_send('_2')

        elif message.text == '/online_list_off' or message.text == '/online_list_off@MySecondLife_bot':
                msg_send('_3')

        elif message.text == '/guest_list' or message.text == '/guest_list@MySecondLife_bot':
                msg_send('_4')

        elif message.text == '/guest_list_on' or message.text == '/guest_list_on@MySecondLife_bot':
                msg_send('_5')

        elif message.text == '/guest_list_off' or message.text == '/guest_list_off@MySecondLife_bot':
                msg_send('_6')
                
        elif message.text != ' ':
            msg_send(message.text)

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