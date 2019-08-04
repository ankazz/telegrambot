import telebot
from telebot import types

bot = telebot.TeleBot("940661668:AAHvHTGP2yUZ2JaS2Hao0wrSvUnHSS5a40Y")
back_menu, back_info, nls, npu = '', '', '', ''
lang = 'kazakh'

languages = {
    'russian': {
        'Start': 'Вас приветствует Бот, выберите в меню что вам интересно!',
        'Lang': 'Сменить язык',
        'Meter': 'Ввести показание',
        'Meter_nls': 'Введите лицевой счет',
        'Meter_ins': 'Введите контрольные показание ПУ',
        'Balans': 'Узнать долг'
    },

    'kazakh': {
       'Start': 'Сізді Бот қарсы алады, мәзірден өзіңізді қызықтыратын нәрсені таңдаңыз!',
       'Lang': 'Тілді өзгерту',
       'Meter': 'Көрсеткішті еңгізу',
       'Meter_nls': 'Дербес шотыңызды еңгізіңіз',
       'Meter_ins': 'Есептегіштің көрсеткісін еңгізіңіз',
       'Balans': 'Қарызды білу'
    },
}

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Принято', reply_markup=main_menu_keyboard())
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Отмена', reply_markup=main_menu_keyboard())

@bot.message_handler(commands=["start"])
def start(m):
    global back_menu, back_info
    # msg = bot.send_message(m.chat.id, languages['kazakh']["Start"])
    bot.send_message(m.chat.id, languages[lang]["Start"], reply_markup=main_menu_keyboard())
    back_menu = main_menu_keyboard()
    back_info = 'Выберите в меню что вам интересно!'
    bot.register_next_step_handler(m, get_name1)


@bot.message_handler(content_types=['text'])
def get_name1(m):
    global back_menu, back_info, lang, nls

    if m.text == 'В начало':
        bot.send_message(m.chat.id, back_info, reply_markup = back_menu)

    if m.text == 'О компании':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.InlineKeyboardButton(text='value', callback_data='value'))
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'инфа о компании',
                         reply_markup=keyboard)
    elif m.text == languages[lang]["Meter"]:
        # nls = m.text
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(m.from_user.id, languages[lang]["Meter_nls"], reply_markup=markup)
        bot.register_next_step_handler(m, InsMeter)

    elif m.text == languages[lang]["Lang"]:
        # global lang
        if lang == 'kazakh':
            lang = 'russian'
        else:
            lang = 'kazakh'

        bot.send_message(m.chat.id, languages[lang]["Start"], reply_markup=main_menu_keyboard())

    elif m.text == 'Одиночный':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'Сожалею, но в данный момент акций нет(', reply_markup=keyboard)

def InsMeter(message):  # получаем фамилию
    global nls
    nls = message.text
    bot.send_message(message.from_user.id, languages[lang]["Meter_ins"])
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global nls, npu
    npu = message.text
    # bot.send_message(message.from_user.id, surname + ' - спасибо за переданное показание', reply_markup=main_menu_keyboard())
    # bot.register_next_step_handler(message, get_name1)

    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Ваш лицевой счет ' + str(nls) + ' лет, к/п ПУ ' + npu + ' все правильно?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

def main_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.InlineKeyboardButton(text=languages[lang]["Balans"], callback_data='balans'), types.InlineKeyboardButton(text=languages[lang]["Meter"], callback_data='meter'))
    keyboard.add(types.InlineKeyboardButton(text='value2', callback_data='value2'))
    keyboard.add(types.InlineKeyboardButton(text=languages[lang]["Lang"], callback_data='lang'))
    return keyboard

bot.polling()