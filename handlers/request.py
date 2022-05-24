from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import commands as db
from keyboards import kb_main, kb_location

class FSMDeliver(StatesGroup):
    adress = State()
    product = State()

async def get_adress(message: types.Message):
    await FSMDeliver.adress.set()
    await message.answer("Введите адресс куда приедет курьер", reply_markup=kb_location)

async def save_adress(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
    await FSMDeliver.next()
    await message.answer("Выберите из какого меню вы хотите заказать продукты(pizza, burgers, sushi, snacks, drink) и номер продукта")
    await message.answer("Пример: sushi 2")

async def products(message: types.Message, state: FSMContext):
    parsed_message = message.text.split(' ')
    async with state.proxy() as data:
            data['product']  = db.select_product(parsed_message[0], parsed_message[1])
    await message.answer(data, reply_markup=kb_main)
    await state.finish()

async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Действие отменено.", reply_markup=kb_main)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(get_adress, commands=['make_request'])
    dp.register_message_handler(cancel, commands=['cancel'] , state='*')
    dp.register_message_handler(save_adress, state=FSMDeliver.adress)
    dp.register_message_handler(products, state=FSMDeliver.product)
    