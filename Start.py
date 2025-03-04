import asyncio
import logging

from aiogram import Bot, Dispatcher, types
#from aiogram.dispatcher.filters import Command  # Correct import for aiogram 2.x
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Замените "YOUR_BOT_TOKEN" на токен, который вы получили от BotFather
API_TOKEN = "7744620926:AAGluQaagdD1-R-XciOdgrP97nL95iiAMvk"

# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()  # Pass `bot` in aiogram 2.x

# Хэндлер на команду /start
# хочу все хэндлеры вынести в отдельный файл
#-----------------------------------------------------------------------------
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я Марк - ботяра. Чекаем квиз /quiz")

# Хэндлер на команду /quiz
@dp.message(Command("quiz"))
async def cmd_quiz(message: types.Message):
    # Логика начала квиза
    await message.answer("Давайте начнем квиз! Первый вопрос: ...")



#-----------------------------------------------------------------------------


# Структура квиза
quiz_data = [
    {
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
    # Добавьте другие вопросы
]

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())