import json
import asyncio
import logging
from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command

# Настройка логгирования (по желанию)
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
API_TOKEN = '6312063401:AAGR82IGEJungfeFA9APSYvUtHkJVrdxoVI'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Путь к JSON-файлу с заявками
JSON_FILE_PATH = 'C:/Users/fortu/OneDrive/Desktop/Сайт автомобили/auto_site/Carshipment/main/Bot/data.json'

# ID пользователя или чата, которому будут отправляться уведомления
ADMIN_CHAT_ID = '711642423'


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("""
Приветсвуем Вас в нашем боте!
        
На данный момент он еще находится в разработке и доступ к нему имеется только у администрации.
        """)
    await check_and_notify(message)


@dp.message(Command("check"))
async def check_and_notify(message: types.Message):
    # Чтение JSON-файла
    while True:
        try:
            with open(JSON_FILE_PATH, 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = []
            await bot.send_message(ADMIN_CHAT_ID, "Нет данных")

        if len(data) != 0:
            # Если есть заявки, отправляем уведомление
            message_text = "Новая заявка поступила:\n"
            for request in data:
                message_text += f"Тема: {request['subject']}\nИмя: {request['name']}\n" \
                                f"Телефон: {request['phone_number']}\n\n"
            
            await bot.send_message(ADMIN_CHAT_ID, message_text)

            # Удаляем заявки из JSON-файла
            data.clear()
            with open(JSON_FILE_PATH, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        
        # Проверка каждые 10 секунд
        await asyncio.sleep(5)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())