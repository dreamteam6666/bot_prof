from aiogram import Bot, Dispatcher, types

from data import config

# токекен бота
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# диспетчер
dp = Dispatcher(bot)