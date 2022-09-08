import telebot
from telebot import types
import random
bot = telebot.TeleBot('5515546524:AAH16V1LKN9soh1IAhjd9TjKpiKg3AOJcog')

first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!",
         "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
         "Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, "Привет чем я могу тебе помочь?")
        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        keyboard.add(key_oven)

        key_oven = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        keyboard.add(key_oven)
        bot.send_message(message.chat.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == '/help':
        bot.send_message(message.chat.id, "Напиши привет")
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю, напиши /help")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "zodiac":
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(
            second_add) + ' ' + random.choice(third)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)



bot.polling(none_stop=True, interval=0)