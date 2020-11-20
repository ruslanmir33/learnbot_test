from glob import glob
import logging
from random import choice

from utils import get_keyboard, get_user_emo



def greet_user(update, context):
    user_data = context.user_data
    emo = get_user_emo(user_data)
    user_data['emo'] = emo
    text = 'Привет {}'.format(emo)
    update.message.reply_text(text, reply_markup = get_keyboard())
    

def talk_to_me(update, context):
    user_data = context.user_data
    emo = get_user_emo(user_data)
    user_text = 'Привет {} {}!Мы поможем с инвестированием. Ты написал: {}'.format(update.message.chat.first_name, emo,
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
