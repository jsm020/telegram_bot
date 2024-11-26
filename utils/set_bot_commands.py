from aiogram import Bot
from aiogram.types import BotCommand

async def set_default_commands(bot: Bot):
    """
    Bot uchun default komandalarni o'rnatadi.
    """
    commands = [
        BotCommand(command="start", description="Botni ishga tushurish"),
        BotCommand(command="help", description="Yordam"),
    ]
    await bot.set_my_commands(commands)
