from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,\
    InlineKeyboardMarkup, InlineKeyboardButton
"""Здесь создаем кнопки"""


def main_reply_keyboard() -> ReplyKeyboardMarkup:
    # Создание кнопок, каждый список внутри равен строке
    # Также работает с Inline кнопками, но там немного по другому
    buttons = [
        [KeyboardButton(text='Первая строка'), KeyboardButton(text='Вторая кнопка в первой строке')],
        [KeyboardButton(text='Вторая строка')],
        [KeyboardButton(text='Третья строка')]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons,
                               resize_keyboard=True,
                               one_time_keyboard=True)  # Обычные кнопки
