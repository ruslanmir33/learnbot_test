from glob import glob
import logging
from random import choice

from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler, Filters

import setting


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                   level=logging.INFO,
                   filename='bot.log'
    )




def greet_user(update, context):
    user_data = context.user_data
    emo = get_user_emo(user_data)
    user_data['emo'] = emo
    text = 'Привет {}'.format(emo)
    update.message.reply_text(text, reply_markup = get_keyboard())
    

def talk_to_me(update, context):
    user_data = context.user_data
    emo = get_user_emo(user_data)
    user_text = 'Привет {} {}! Ты написал: {}'.format(update.message.chat.first_name, emo,
                   update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                 update.message.chat.id, update.message.text)
    update.message.reply_text(user_text, reply_markup = get_keyboard())

def send_money_picture(update, context):
    money_list = glob('images/*.jp*g')
    money_pic = choice(money_list)
    bot=context.bot
    bot.send_photo(chat_id = update.message.chat_id, photo = open(money_pic, 'rb'), reply_markup = get_keyboard())
    
def change_avatar(update, context):
    user_data = context.user_data
    if 'emo' in user_data:
        del user_data['emo']
    emo = get_user_emo(user_data)
    update.message.reply_text('Готово: {}'.format(emo), reply_markup = get_keyboard())

def get_contact(update, context):
    user_data = context.user_data
    print(update.message.contact)
    update.message.reply_text('Готово: {}'.format(get_user_emo(user_data)), reply_markup = get_keyboard())

def get_location(update, context):
    user_data = context.user_data
    print(update.message.location)
    update.message.reply_text('Готово: {}'.format(get_user_emo(user_data)), reply_markup = get_keyboard())


def get_user_emo(user_data):
    if 'emo'in user_data:
        return user_data['emo']
    else:
        user_data['emo'] = emojize(choice(setting.USER_EMOJI), use_aliases = True)
        return user_data['emo']

def get_keyboard():
    contact_button = KeyboardButton('Прислать контакты', request_contact=True)
    location_buton = KeyboardButton('Прислать координаты', request_location = True)
    my_keyboard = ReplyKeyboardMarkup([['Прислать деньги', 'Сменить аватарку'],
                                        [contact_button, location_buton]
                                      ], resize_keyboard=True
                                      )
    return my_keyboard
    


def main():
    mybot = Updater(setting.API_KEY, use_context=True)

    logging.info('Бот запускается')
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('money', send_money_picture, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать деньги)$'), send_money_picture, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex('^(Сменить аватарку)$'), change_avatar, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))
    


    mybot.start_polling()
    mybot.idle()



if __name__ == "__main__":
    main()

