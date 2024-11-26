from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# ReplyKeyboard
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Salom")],
        [KeyboardButton(text="Yordam")],
        [KeyboardButton(text="Qo'shimcha ma'lumot")],
    ],
    resize_keyboard=True
)

# InlineKeyboard
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Google", url="https://google.com")],
        [InlineKeyboardButton(text="Callback Tugma", callback_data="callback_data_test")],
    ]
)
