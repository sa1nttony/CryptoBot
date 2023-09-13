import telebot
from config import keys, TOKEN, commands
from utils import ConvertionException, CryptoConverter


bot = telebot.TeleBot(TOKEN)

quote = None
base = None
amount = None
markup = None


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = f'Бот предназначен для быстрой проверки курса валют. \n' \
           f'Доступные команды:\n'
    counter = 1
    for i in [*commands]:
        cmnd = f'{counter}. {i} - {commands[i]}\n'
        text = text + cmnd
        counter += 1
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    counter = 1
    for key in keys.keys():
        l_key = key
        key_1 = l_key[0].upper()
        key_1 = key_1.upper()
        key = key_1 + l_key[1::]
        text = f'\n{counter}. '.join((text, key, ))
        counter += 1
    bot.reply_to(message, text)


@bot.message_handler(commands=['convert'])
def start_convert(message: telebot.types.Message):
    global markup, markup
    set_buttons()
    msg = bot.send_message(message.chat.id, f'Выберите валюту', reply_markup=markup)
    bot.register_next_step_handler(msg, set_quote)


@bot.message_handler(content_types=['text', 'sticker', 'video', 'video_note', 'voice'])
def i_am_busy(message: telebot.types.Message):
    text = 'Извини, но я слежу за курсами валют и не могу сейчас говорить. \nЛучше спроси меня об актуальных курсах'
    bot.reply_to(message, text)


def set_quote(message):
    global quote, markup
    set_buttons()
    quote = message.text.lower()
    msg = bot.send_message(message.chat.id,
                           f'В какую валюту будем переводить {quote}?', reply_markup=markup)
    bot.register_next_step_handler(msg, set_base)


def set_base(message):
    global base, markup
    set_buttons(empty=True)
    base = message.text.lower()
    msg = bot.send_message(message.chat.id,
                           'Введите количество вводимой валюты', reply_markup=markup)
    bot.register_next_step_handler(msg, set_amount)


def set_amount(message):
    global quote, base, amount
    try:
        amount = float(message.text.lower())
    except ValueError:
        amount = '1'
    converter(quote, base, amount, message)


def converter(quote, base, amount, message):
    try:
        price = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Введена неизвестная команда')
    else:
        text = f'{amount} {keys[quote]} = {price} {keys[base]}'
        bot.send_message(message.chat.id, text)


def set_buttons(empty=False):
    global markup
    if not empty:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        buttons = [*keys]
        for i in buttons:
            l_btn = i
            btn_1 = l_btn[0].upper()
            btn_1 = btn_1.upper()
            btn = btn_1 + l_btn[1::]
            markup.add(btn)
    else:
        markup = telebot.types.ReplyKeyboardRemove()


bot.polling(none_stop=True)
