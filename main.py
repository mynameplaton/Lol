import telebot
import random
from telebot import types

token = "Я вам не скажу мой токен лол"
bot = telebot.TeleBot(token)

tips = [
    "Выключай свет, когда выходишь из комнаты",
    "Используй многоразовую бутылку для воды",
    "Не оставляй зарядку в розетке",
    "Экономь воду дома"
]

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Температура", "co2")
    keyboard.add("Ледники", "совет")

    bot.send_message(
        message.chat.id,
        "Привет! я хранитель планеты 🌍\n"
        "Выбери, что хочешь узнать:",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def answer(message):
    text = message.text.lower()

    if text == "температура":
        bot.send_message(
            message.chat.id,
            "Средняя температура земли выросла примерно на 1°c."
        )

    elif text == "co2":
        bot.send_message(
            message.chat.id,
            "Уровень co2 в атмосфере превышает 420 ppm."
        )

    elif text == "ледники":
        bot.send_message(
            message.chat.id,
            "Арктические льды сокращаются с каждым годом."
        )

    elif text == "совет":
        bot.send_message(
            message.chat.id,
            "Совет дня 🌱: " + random.choice(tips)
        )

    else:
        bot.send_message(
            message.chat.id,
            "Я не понял сообщение, выбери кнопку 🙂"
        )

bot.polling()
