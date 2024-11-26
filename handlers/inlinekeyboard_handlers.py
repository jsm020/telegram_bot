from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardRemove
import asyncio

# Routerni yaratamiz
router = Router()

@router.callback_query(lambda callback: callback.data == "callback_data_test")
async def callback_handler(callback: CallbackQuery):
    """
    Callback ishlovchi. Faqat 'callback_data_test' text bilan kelgan callbacklarni ishlaydi.
    """
    # Foydalanuvchiga javob yuborish va reply tugmalarni olib tashlash
    await callback.message.answer(
        "Callback ishladi! 1 daqiqadan keyin inline tugmalar o'chiriladi.",
        reply_markup=ReplyKeyboardRemove()  # ReplyKeyboardni olib tashlash
    )

    # 1 daqiqa kutish
    await asyncio.sleep(60)

    # Inline tugmalarni olib tashlash
    try:
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.answer("Inline tugmalar o'chirildi.")
    except Exception as e:
        print(f"Tugmalarni o'chirishda xatolik: {e}")

# Routerni registratsiya qilish
def register_inlinekeyboard_handlers(dp):
    dp.include_router(router)
