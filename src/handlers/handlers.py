from logging import info
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.kb import menu
from text.text import hi_message

router = Router()


# команда старт
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(f"{hi_message}")


# команда меню
@router.message(Command("menu"))
async def menu_handler(msg: Message):
    await msg.answer( menu)


# команда информации
@router.message(Command("info"))
async def info_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")