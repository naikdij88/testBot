#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from constants import Data 

def main():
    bot = telebot.TeleBot(Data.token)

    @bot.message_handler(content_types=['text'])
    def send_welcome(message):
        if message.text == '/sl':
            bot.reply_to(message, "b")

        elif message.text == 'b':
            bot.reply_to(message, "a")
    

    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
            exit()