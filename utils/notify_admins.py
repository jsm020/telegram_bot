import logging
from aiogram import Bot

async def on_startup_notify(bot: Bot, admins: list):
    """
    Adminlarga bot ishga tushgani haqida xabar yuboradi.
    """
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, "Bot ishga tushdi")
        except Exception as err:
            logging.exception(f"Admin {admin_id} ga xabar yuborishda xatolik: {err}")
