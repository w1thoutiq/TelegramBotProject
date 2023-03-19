from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ContentType, ParseMode
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from os import environ as env
from Functions import *
from DataBase import *
from Buttons import *
import logging

"""Основной файл с ботом"""
"""Нужно над текстом еще поработать"""

logging.basicConfig(level=logging.INFO)
bot = Bot(token=env['token_name'], parse_mode=ParseMode.HTML)
storage = MemoryStorage()  # Хранилище
dp = Dispatcher(bot, storage=storage)


class States(StatesGroup):
    first = State()
    second = State()
    third = State()
    fourth = State()
    fifth = State()


# Обработка команды start
@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext) -> bot.send_message:
    await state.finish()  # Завершение машины состояний
    cur.execute("SELECT user_id FROM telegram")
    if message.from_user.id not in [user[0] for user in cur.fetchall()]:  # Проверка наличия id в базе
        input_on_bd(message.from_user.id,
                    message.from_user.username)  # Заполнение БД
        return await message.answer(
            text=f'Привет, <b>{message.from_user.first_name}</b>! 🖐\n'
                 f'Тут дальше что-то будет',
            parse_mode=ParseMode.HTML,
            reply_markup=main_reply_keyboard())
    else:
        await message.answer(text=f'Привет, <b>{message.from_user.first_name}</b>!🖐',
                             parse_mode=ParseMode.HTML,
                             reply_markup=main_reply_keyboard())


@dp.message_handler(commands=['help'], state=None)
async def cmd_help(message: types.Message) -> bot.send_message:
    return await message.answer(
        text=f'Все команды которые я понимаю:\n'
             f'Тут команды')


@dp.message_handler(Text(equals='привет', ignore_case=True))
async def cmd_help(message: types.Message) -> bot.send_message:
    return await message.answer(
        text=f'Привет, <b>{message.from_user.first_name}</b> 🖐'
    )


# Обработка любого типа сообщения, должна быть самой последней функцией
@dp.message_handler(content_types=ContentType.ANY, state='*')
async def any_text(message: types.Message) -> bot.send_message:
    return await bot.send_message(
        chat_id=message.from_user.id,
        text=f'Я не понял что ты имеешь ввиду, но ты можешь написать команду /help, '
             f'что бы увидеть все команды')


if __name__ == "__main__":
    executor.start_polling(dp)  # Бесконечный цикл для работы бота
