from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


cube = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/idonotknow")
        ],
        [
            KeyboardButton(text="/iknow")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
