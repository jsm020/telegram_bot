from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.using_state import Form
from aiogram.filters import Command

router = Router()

# /start komandasini ishlashga tayyorlaymiz
@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    await message.answer("Ismingizni kiriting:")
    await state.set_state(Form.waiting_for_name)  # Holatni "waiting_for_name"ga o'rnatamiz

# Ismni olish va keyingi holatga o'tish
@router.message(Form.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)  # Ismni saqlaymiz
    await message.answer("Endi yoshingizni kiriting:")
    await state.set_state(Form.waiting_for_age)  # Holatni "waiting_for_age"ga o'zgartiramiz

# Yoshni olish va barcha ma'lumotlarni qaytarish
@router.message(Form.waiting_for_age)
async def process_age(message: Message, state: FSMContext):
    user_data = await state.get_data()  # Avvalgi holatda saqlangan ma'lumotlarni olamiz
    name = user_data.get("name")
    age = message.text

    await message.answer(f"Rahmat! Sizning ismingiz: {name}, yoshingiz: {age}.")
    await state.clear()  # Holatni tozalaymiz

def register_state_handlers(dp):
    dp.include_router(router)
