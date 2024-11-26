from aiogram import Router
from aiogram.types import Message
from keyboards.main_keyboard import inline_keyboard

router = Router()

@router.message(lambda message: message.text == "Salom")
async def handle_hello(message: Message):
    await message.answer("Salom, foydalanuvchi!")

@router.message(lambda message: message.text == "Yordam")
async def handle_help(message: Message):
    await message.answer("Yordamga muhtojmisiz?")

@router.message(lambda message: message.text == "Qo'shimcha ma'lumot")
async def handle_info(message: Message):
    await message.answer("Bu bot sizga xizmat ko'rsatish uchun yaratilgan.", reply_markup=inline_keyboard)

def register_keyboard_handlers(dp):
    dp.include_router(router)
