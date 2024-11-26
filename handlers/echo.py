from aiogram import Router
from aiogram.types import Message

# Router yaratamiz
echo_router = Router()

@echo_router.message()
async def echo_message(message: Message):
    await message.answer(f"Sizning xabaringiz: {message.text}")

# Routerni registratsiya qilish funksiyasi
def register_echo_handlers(dp):
    dp.include_router(echo_router)
