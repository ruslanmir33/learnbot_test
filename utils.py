from random import choice

from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton

import setting

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