from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,\
    InlineKeyboardMarkup, InlineKeyboardButton

"""Здесь создаем кнопки"""


def main_reply_keyboard() -> ReplyKeyboardMarkup:
    # Создание кнопок, каждый список внутри равен строке
    buttons = [
        [KeyboardButton(text='text')],
        [KeyboardButton(text='text')],
        [KeyboardButton(text='text')]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons)  # Создание разметки под местом ввода
