from aiogram.types import ReplyKeyboardMarkup

from data.config import ADMINS as admins


def check_user_out_func(user_id):
    menu_default = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_default.row("Смотреть формулы", "🖍 Добавить формулы", "ℹ FAQ")
    if str(user_id) in admins:
        menu_default.row("Управление формулами")
    return menu_default


all_back_to_main_default = ReplyKeyboardMarkup(resize_keyboard=True)
all_back_to_main_default.row("⬅ На главную")
