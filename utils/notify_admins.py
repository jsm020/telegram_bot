import logging
from aiogram import Bot

async def on_startup_notify(bot: Bot, admins: list):
    """
    Bot send to all admins "Bot is started"
    """
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, "Bot is started")
        except Exception as err:
            logging.exception(f"Admin {admin_id} ga xabar yuborishda xatolik: {err}")
