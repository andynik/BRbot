# -*- coding: utf-8 -*-

import config
import telebot
import vk
import sys


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Hi there! I could tell u smth about your friends b-days.\nWhat's your vk-id? ")

@bot.message_handler(content_types=["text"])
def reply(message):
    try:
        my_id = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, "Invalid id! Please use digits only.\nSo what is your id? ")
        return
    bot.send_message(message.chat.id, "OK")

    session = vk.Session()
    api = vk.API(session)
    friend_ids = api.friends.get(user_id=my_id)


    bot.send_message(message.chat.id, "Here some of your friends birthdays:")
    cnt = 0
    for friend_id in friend_ids:
        friend_info = api.users.get(user_ids=friend_id, fields="bdate")[0]
        print(friend_info)
        if 'bdate' in friend_info:
            ans = friend_info['first_name'] + ' ' + friend_info['last_name'] + ' was born in ' + friend_info['bdate']
            bot.send_message(message.chat.id, ans)

            cnt += 1
            if cnt == min(len(friend_ids), config.n):
                break


if __name__ == '__main__':
     bot.polling(none_stop=True)
