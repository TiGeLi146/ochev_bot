from aiogram.types import ReplyKeyboardMarkup

items_default = ReplyKeyboardMarkup(resize_keyboard=True)
items_default.row("Добавить формулы", "Изменить формулы", "Удалить формулы")
items_default.row("Создать категорию", "Изменить категорию", "Удалить категории")
items_default.row("⬅ На главную")

finish_load_items_default = ReplyKeyboardMarkup(resize_keyboard=True)
finish_load_items_default.row("Закончить добавление")
