from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Удаление категорий
confirm_clear_category_inl = InlineKeyboardMarkup()
yes_clear_cat_kb = InlineKeyboardButton(text="❌ Да, удалить все", callback_data="confirm_clear_category")
not_clear_cat_kb = InlineKeyboardButton(text="✅ Нет, отменить", callback_data="cancel_clear_category")
confirm_clear_category_inl.add(yes_clear_cat_kb, not_clear_cat_kb)

# Удаление формул
confirm_clear_position_inl = InlineKeyboardMarkup()
yes_clear_cat_kb = InlineKeyboardButton(text="❌ Да, удалить все", callback_data="confirm_clear_position")
not_clear_cat_kb = InlineKeyboardButton(text="✅ Нет, отменить", callback_data="cancel_clear_position")
confirm_clear_position_inl.add(yes_clear_cat_kb, not_clear_cat_kb)
