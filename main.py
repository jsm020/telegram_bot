from handlers.start_handler import register_start_handlers
from handlers.keyboard_handler import register_keyboard_handlers
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession
from config import BOT_TOKEN,ADMINS
from handlers import start_handler, echo
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
async def main():
    # Botni sozlash
    session = AiohttpSession()
    bot = Bot(token=BOT_TOKEN, session=session)
    dp = Dispatcher(storage=MemoryStorage())

    # Komandalarni o'rnatamiz
    await set_default_commands(bot)
    await on_startup_notify(bot, ADMINS)
    # Handerlarni registratsiya qilamiz
    register_start_handlers(dp)
    register_keyboard_handlers(dp)
    echo.register_echo_handlers(dp)
    # Pollingni boshlaymiz
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
