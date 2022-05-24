import logging
from bot_crt import dp
from aiogram import executor
from handlers import menu, request, comment, start

logging.basicConfig(level=logging.INFO)


request.register_handlers(dp)
start.register_handlers(dp)
menu.register_handlers(dp)
comment.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)