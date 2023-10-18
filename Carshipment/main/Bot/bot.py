import json
import asyncio
import logging
from aiogram import Bot, types
from aiogram import Dispatcher

# Настройка логгирования (по желанию)
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
API_TOKEN = '6312063401:AAGR82IGEJungfeFA9APSYvUtHkJVrdxoVI'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Путь к JSON-файлу с заявками
JSON_FILE_PATH = 'data.json'

# ID пользователя или чата, которому будут отправляться уведомления
ADMIN_CHAT_ID = '@Nikita4156'

async def check_and_notify():
    while True:
        # Чтение JSON-файла
        try:
            with open(JSON_FILE_PATH, 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = []

        if data:
            # Если есть заявки, отправляем уведомление
            message_text = "Новая заявка поступила:\n"
            for request in data:
                message_text += f"Тема: {request['subject']}\nИмя: {request['name']}\nТелефон: {request['phone_number']}\n\n"
            
            await bot.send_message(ADMIN_CHAT_ID, message_text)

            # Удаляем заявки из JSON-файла
            data.clear()
            with open(JSON_FILE_PATH, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        
        # Проверка каждые 10 секунд
        await asyncio.sleep(10)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(check_and_notify())
    
    try:
        loop.run_until_complete(dp.start_polling(skip_updates=True))
    finally:
        loop.run_until_complete(dp.bot.session.close())