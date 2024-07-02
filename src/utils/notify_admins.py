from cgitb import text
import logging

from aiogram import Dispatcher

from data.config import ADMINS_ID


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS_ID:
        try:
            text = "Бот запусщен!"
            await dp.bot.send_message(chat_id=admin, text=text)

        except Exception as error:
            logging.exception(error) 
            # logging.error(f"Ошибка при отправке сообщения: {error}")