import telebot
import random
from telebot import types

token = "TOKEN"
bot = telebot.TeleBot(token)

# Советы
tips = [
    "выключай свет, когда выходишь из комнаты",
    "используй многоразовую бутылку для воды",
    "не оставляй зарядку в розетке",
    "экономь воду дома"
]

user_messages = {}

# Словарь с картинками для каждой кнопки
images = {
    "температура": "images/temperature.jpg",
    "co2": "images/co2.png",
    "ледники": "images/glacier.jpg",
    "совет": "images/eco.jpg"
}

@bot.message_handler(commands=["start"])
def start(message):
    user_messages[message.chat.id] = 0

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("температура", "co2")
    keyboard.add("ледники", "совет")
    keyboard.add("статистика", "помощь")

    bot.send_message(
        message.chat.id,
        "привет! я хранитель планеты 🌍\n"
        "выбери действие:",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def answer(message):
    chat_id = message.chat.id
    text = message.text.lower()

    if chat_id not in user_messages:
        user_messages[chat_id] = 0

    user_messages[chat_id] += 1

    if text in images:
        # Отправляем картинку по ключу
        with open(images[text], "rb") as photo:
            bot.send_photo(chat_id, photo)

        # Отправляем текст после картинки
        if text == "температура":
            bot.send_message(chat_id, "температура земли выросла примерно на 1°c.")
        elif text == "co2":
            bot.send_message(chat_id, "уровень co2 превышает 420 ppm.")
        elif text == "ледники":
            bot.send_message(chat_id, "арктические льды тают каждый год.")
        elif text == "совет":
            bot.send_message(chat_id, "совет дня 🌱: " + random.choice(tips))

    elif text == "статистика":
        bot.send_message(
            chat_id,
            f"ты написал боту {user_messages[chat_id]} сообщений 🙂"
        )

    elif text == "помощь":
        bot.send_message(
            chat_id,
            "я показываю данные о климате и даю советы 🌍\n"
            "кнопки:\n"
            "температура — про потепление\n"
            "co2 — про углекислый газ\n"
            "ледники — про арктику\n"
            "совет — экосовет\n"
            "статистика — сколько ты писал боту"
        )

    else:
        bot.send_message(chat_id, "используй кнопки ниже")

bot.infinity_polling()
