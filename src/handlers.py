from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from kb import menu
from text import hi_message

router = Router()


# команда старт
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(f"{hi_message}")


# команда меню
@router.message(Command("menu"))
async def start_handler(msg: Message):
    await msg.answer("Меню", menu)


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")