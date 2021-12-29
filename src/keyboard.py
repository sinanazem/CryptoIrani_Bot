from telebot import types

def create_keybord(key,row_width=2,resize_keyboard=True):
    markup = types.ReplyKeyboardMarkup(row_width=row_width,resize_keyboard=resize_keyboard)
    button = types.KeyboardButton('Bitcoin')
    markup.add(button)
    return markup
