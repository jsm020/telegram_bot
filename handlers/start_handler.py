from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.main_keyboard import main_keyboard

router = Router()

@router.message(Command(commands=["start"]))
async def start_command(message: Message):
    await message.answer(
        "Assalomu alaykum! Botga xush kelibsiz!",
        reply_markup=main_keyboard
    )

def register_start_handlers(dp):
    dp.include_router(router)
