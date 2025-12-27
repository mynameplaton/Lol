import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "No"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add("🌡️ Температура", "🫁 CO₂")
kb.add("❄️ Ледники", "♻️ Совет")

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer(
        "Привет! Я EcoInfoBot 🌍\nВыбери действие:",
        reply_markup=kb
    )

@dp.message_handler(lambda m: m.text == "🌡️ Температура")
async def temp(m: types.Message):
    await m.answer("Средняя температура Земли растёт.")

@dp.message_handler(lambda m: m.text == "🫁 CO₂")
async def co2(m: types.Message):
    await m.answer("Уровень CO₂ в атмосфере увеличивается.")

@dp.message_handler(lambda m: m.text == "❄️ Ледники")
async def ice(m: types.Message):
    await m.answer("Арктические ледники тают.")
@dp.message_handler(lambda m: m.text == "♻️ Совет")
async def tip(m: types.Message):
    tips = [
        "Экономь воду",
        "Выключай свет",
        "Используй многоразовые вещи"
    ]
    await m.answer(random.choice(tips))

if __name__ == "__main__":
    executor.start_polling(dp)
