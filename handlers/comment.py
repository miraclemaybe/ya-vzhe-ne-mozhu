from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import commands as db
from keyboards import kb_menu, kb_main

async def send_reviews(message: types.Message):
    answer = ''
    reviews = db.select_reviews()
    for review in reviews:
        answer = answer + 'Кто оставил: ' + review[0] + ' Отзыв: ' + review[1] + '\n'
    await message.answer(answer)

def register_handlers(dp: Dispatcher):
   dp.register_message_handler(send_reviews, commands=['reviews'])