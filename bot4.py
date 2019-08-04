import telebot
from telebot import types

bot = telebot.TeleBot("940661668:AAHvHTGP2yUZ2JaS2Hao0wrSvUnHSS5a40Y")


@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Вас приветствует Бот")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['О компании', 'Прайс-лист']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Акции', 'Контакты']])
    bot.send_message(m.chat.id, 'Выберите в меню что вам интересно!',
        reply_markup=keyboard)
    bot.register_next_step_handler(msg, get_name)


@bot.message_handler(content_types=['text'])
def get_name(m):
    back_menu = m.text
    if m.text == 'О компании':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.InlineKeyboardButton(text='value', callback_data='value'))
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'инфа о компании',
                         reply_markup=keyboard)
    elif m.text == 'Прайс-лист':

        bot.send_message(m.chat.id, 'Выберите прайс который нужен.',
                         reply_markup=keyboard)
    elif m.text == 'Акции':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'Сожалею, но в данный момент акций нет(',
                         reply_markup=keyboard)

    elif m.text == 'Одиночный':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'Сожалею, но в данный момент акций нет(',
                         reply_markup=keyboard)

    elif m.text == 'В начало':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'Сожалею, но в данный момент акций нет(',
                         reply_markup=keyboard)


def main_menu_keyboard():
  keyboard = [[types.KeyboardButton('Option 1', callback_data='m1')],
              [types.KeyboardButton('Option 2', callback_data='m2')],
              [types.KeyboardButton('Option 3', callback_data='m3')]]
  return types.KeyboardButton(keyboard)

def first_menu_keyboard():
  keyboard = [[types.KeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [types.KeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [types.KeyboardButton('Main menu', callback_data='main')]]
  return types.KeyboardButton(keyboard)

def second_menu_keyboard():
  keyboard = [[types.KeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [types.KeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [types.KeyboardButton('Main menu', callback_data='main')]]
  return types.KeyboardButton(keyboard)

bot.polling()