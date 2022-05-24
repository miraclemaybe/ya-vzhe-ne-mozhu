from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_request = KeyboardButton('make request')
button_menu = KeyboardButton('menu')
button_cancel = KeyboardButton('cancel')
button_location = KeyboardButton('send location', request_location=True)
button_feedbacks = KeyboardButton('feedbacks')
button_give_feedbacks = KeyboardButton('give feedback')

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(button_request).add(button_menu).add(button_feedbacks).add(button_give_feedbacks)

kb_location = ReplyKeyboardMarkup(resize_keyboard=True)
kb_location.add(button_cancel).add(button_location)


button_pizza = KeyboardButton('pizza')
button_sushi = KeyboardButton('sushi')
button_potato = KeyboardButton('snacks')

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.add(button_pizza).add(button_sushi).add(button_potato)


kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)