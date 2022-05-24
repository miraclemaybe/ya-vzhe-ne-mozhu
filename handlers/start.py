from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from keyboards import kb_main

async def help(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!", reply_markup=kb_main)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(help, commands=['start', 'help'])