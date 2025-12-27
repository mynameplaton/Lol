import telebot

token = "I'm not telling you my token"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "привет! я хранитель планеты 🌍\n"
        "команды:\n"
        "/temp — температура\n"
        "/co2 — co2\n"
        "/ice — ледники\n"
        "/tip — совет"
    )

@bot.message_handler(commands=["temp"])
def temp(message):
    bot.send_message(message.chat.id, "температура земли выросла примерно на 1°c.")

@bot.message_handler(commands=["co2"])
def co2(message):
    bot.send_message(message.chat.id, "уровень co2 сейчас больше 420 ppm.")

@bot.message_handler(commands=["ice"])
def ice(message):
    bot.send_message(message.chat.id, "арктические льды тают каждый год.")

@bot.message_handler(commands=["tip"])
def tip(message):
    bot.send_message(message.chat.id, "совет 🌱: выключай свет, когда выходишь из комнаты.")

bot.polling()
