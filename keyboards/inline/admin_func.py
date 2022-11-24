from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.sqlite import get_positionx, get_positionsx, get_categoryx


def edit_category_func(category_id, remover):
    category_keyboard = InlineKeyboardMarkup()
    get_fat_count = len(get_positionsx("*", category_id=category_id))
    get_category = get_categoryx("*", category_id=category_id)

    messages = "<b>Выберите действие с категорией</b>\n" \
               "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
               f"Название: <code>{get_category[2]}</code>\n" \
               f"Кол-во формул: <code>{get_fat_count}шт</code>"

    change_name_kb = InlineKeyboardButton(text="Изменить название",
                                          callback_data=f"category_edit_name:{category_id}:{remover}")
    remove_kb = InlineKeyboardButton(text="Удалить",
                                     callback_data=f"category_remove:{category_id}:{remover}")
    back_category_kb = InlineKeyboardButton("Вернуться",
                                            callback_data=f"back_category_edit:{remover}")
    category_keyboard.add(change_name_kb, remove_kb)
    category_keyboard.add(back_category_kb)
    return messages, category_keyboard


def confirm_remove_func(category_id, remover):
    confirm_remove_keyboard = InlineKeyboardMarkup()
    change_name_kb = InlineKeyboardButton(text="Да, удалить",
                                          callback_data=f"yes_remove_category:{category_id}:{remover}")
    move_kb = InlineKeyboardButton(text="Нет, отменить",
                                   callback_data=f"not_remove_category:{category_id}:{remover}")
    confirm_remove_keyboard.add(change_name_kb, move_kb)
    return confirm_remove_keyboard


def open_edit_position_func(position_id, category_id, remover):
    open_item_keyboard = InlineKeyboardMarkup()
    get_position = get_positionx("*", position_id=position_id)

    messages = "<b>Редактирование формулы:</b>\n" \
               "➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
               f"<b>Название:</b> <code>{get_position[2]}</code>\n" \
               f"<b>Формула:</b> <code>{get_position[3]}</code>\n"
    edit_name_kb = InlineKeyboardButton(text="Изм. название",
                                        callback_data=f"position_change_name:{position_id}:{category_id}:{remover}")
    edit_price_kb = InlineKeyboardButton(text="Изм. формулу",
                                         callback_data=f"position_change_price:{position_id}:{category_id}:{remover}")
    remove_kb = InlineKeyboardButton(text="Удалить",
                                     callback_data=f"position_remove_this:{position_id}:{category_id}:{remover}")
    back_positions_kb = InlineKeyboardButton("Вернуться",
                                             callback_data=f"back_position_edit:{category_id}:{remover}")
    open_item_keyboard.add(edit_name_kb, edit_price_kb)
    open_item_keyboard.add(remove_kb)
    open_item_keyboard.add(back_positions_kb)
    return messages, open_item_keyboard


def confirm_remove_position_func(position_id, category_id, remover):
    confirm_remove_position_keyboard = InlineKeyboardMarkup()
    change_name_kb = InlineKeyboardButton(text="Да, удалить",
                                          callback_data=f"yes_remove_position:{position_id}:{category_id}:{remover}")
    move_kb = InlineKeyboardButton(text="Нет, отменить",
                                   callback_data=f"not_remove_position:{position_id}:{category_id}:{remover}")
    confirm_remove_position_keyboard.add(change_name_kb, move_kb)
    return confirm_remove_position_keyboard
