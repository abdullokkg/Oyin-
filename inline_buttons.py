from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menuMain = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text="Brawl stars", callback_data="courses")
        ],
        [
           InlineKeyboardButton(text="Другие игры", callback_data="books")    
        ],
        [
           InlineKeyboardButton(text="Мои заказы", callback_data="gems")
        ],
        [
           InlineKeyboardButton(text="Бот с акциями", callback_data="donat")
        ],
        [
           InlineKeyboardButton(text="Бесплатные гемы", callback_data="bs"),
           InlineKeyboardButton(text="Больше информации", callback_data="cs")
        ]
    ]
)


asosiymenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text="30 гемов", callback_data="ff")
        ]
    ]
)