from dotenv import load_dotenv
import os
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")  # .env dan yoki o'zgaruvchi orqali yuklash
ADMINS = os.getenv("ADMINS", "")  # Agar yo'q bo'lsa, bo'sh satr qaytaradi
ADMINS = [int(admin.strip()) for admin in ADMINS.split(",") if admin.strip().isdigit()]