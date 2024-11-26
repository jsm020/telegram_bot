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
            logging.exception(f"ERROR.{err}. sending message to {admin_id}")
