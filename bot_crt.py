from aiogram import Bot, Dispatcher
import littlesecret
from aiogram.contrib.fsm_storage.memory import MemoryStorage 

storage = MemoryStorage()
bot = Bot(token=littlesecret.API_TOKEN)
dp = Dispatcher(bot, storage=storage)