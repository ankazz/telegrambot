import telebot
from telebot.types import Message
from telebot import types

bot = telebot.TeleBot("940661668:AAHvHTGP2yUZ2JaS2Hao0wrSvUnHSS5a40Y")

name = '';
surname = '';
age = 0;
stringList = {"Name": "John", "Language": "Python", "API": "pyTelegramBotAPI"}


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    print(call.data)
    for key, value in stringList.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if value == call.data:
            print(key)

    if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
        ...  # код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню : )');
    elif call.data == "no":
        ...  # переспрашиваем


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name);  # следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');


def get_name(message):  # получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);


def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);


def get_age(message):
    global age;
    while age == 0:  # проверяем что возраст изменился
        try:
            age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');

    keyboard = types.InlineKeyboardMarkup();  # наша клавиатура

    for key, value in stringList.items():
        keyboard.add(types.InlineKeyboardButton(text=value, callback_data=value),
                     types.InlineKeyboardButton(text='x', callback_data="['key', '" + key + "']"))

    question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?';
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


bot.polling()