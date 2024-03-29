from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.sqlite import *

count_page = 10


################################################################################################
################################# СТРАНИЦЫ ИЗМЕНЕНИЯ КАТЕГОРИЙ #################################
# Стартовые страницы выбора категории для изменения
def category_open_edit_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"edit_category_here:{get_categories[a][1]}:{remover}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page and remover < 10:
        number_of_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_catategory_nextp:{remover + count_page}")
        keyboard.add(number_of_kb, next_kb)
    elif remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_catategory_prevp:{remover - count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, number_of_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_catategory_nextp:{remover + count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_catategory_prevp:{remover - count_page}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    return keyboard


# Следующая страница выбора категории для изменения
def category_edit_next_page_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"edit_category_here:{get_categories[a][1]}:{remover}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_catategory_prevp:{remover - count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, number_of_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_catategory_nextp:{remover + count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_catategory_prevp:{remover - count_page}")
        keyboard.add(prev_kb, number_of_kb, next_kb)

    return keyboard


# Предыдующая страница выбора категории для изменения
def category_edit_prev_page_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"edit_category_here:{get_categories[a][1]}:{remover}"))
        x += 1
    if remover <= 0:
        number_of_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_catategory_nextp:{remover + count_page}")
        keyboard.add(number_of_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"edit_catategory_nextp:{remover + count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"edit_catategory_prevp:{remover - count_page}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    return keyboard


################################################################################################
################################### СТРАНИЦЫ СОЗДАНИЯ ФОРМУЛ ##################################
# Стартовые страницы выбора категории для добавления формулы
def position_open_create_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"create_position_here:{get_categories[a][1]}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page:
        number_of_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_position_nextp:{remover + count_page}")
        keyboard.add(number_of_kb, next_kb)
    return keyboard


# Следующая страница выбора категории для добавления формулы
def position_create_next_page_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"create_position_here:{get_categories[a][1]}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"create_position_prevp:{remover - count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, number_of_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_position_nextp:{remover + count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"create_position_prevp:{remover - count_page}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    return keyboard


# Предыдущая страница выбора категории для добавления формулы
def position_create_previous_page_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"create_position_here:{get_categories[a][1]}"))
        x += 1
    if remover <= 0:
        number_of_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_position_nextp:{remover + count_page}")
        keyboard.add(number_of_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡", callback_data=f"create_position_nextp:{remover + count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅", callback_data=f"create_position_prevp:{remover - count_page}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    return keyboard


################################################################################################
################################## СТРАНИЦЫ ИЗМЕНЕНИЯ ФОРМУЛ ##################################
########################################### Категории ##########################################
# Стартовые страницы категорий при изменении формулы
def position_open_edit_category_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"position_edit_category:{get_categories[a][1]}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page and remover < 10:
        number_of_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_category_nextp:{remover + count_page}")
        keyboard.add(number_of_kb, next_kb)
    elif remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_category_prevp:{remover - count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, number_of_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_category_nextp:{remover + count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    return keyboard


# Следующая страница категорий при изменении формулы
def position_edit_next_page_category_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"position_edit_category:{get_categories[a][1]}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_category_prevp:{remover - count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, number_of_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_category_nextp:{remover + count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    return keyboard


# Предыдущая страница категорий при изменении формулы
def position_edit_previous_page_category_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"position_edit_category:{get_categories[a][1]}"))
        x += 1
    if remover <= 0:
        number_of_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_category_nextp:{remover + count_page}")
        keyboard.add(number_of_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_category_nextp:{remover + count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    return keyboard


########################################### Формулы ##########################################
# Стартовые страницы формул для их изменения
def position_open_edit_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_formulas = get_formulasx("*", category_id=category_id)
    for a in range(remover, len(get_formulas)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_formulas[a][2]} | {get_formulas[a][3]}",
                                              callback_data=f"position_edit:{get_formulas[a][1]}:{remover}:{category_id}"))
        x += 1
    if len(get_formulas) <= 10:
        pass
    elif len(get_formulas) > count_page and remover < 10:
        number_of_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_nextp:{remover + count_page}:{category_id}")
        keyboard.add(number_of_kb, next_kb)
    elif remover + count_page >= len(get_formulas):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_prevp:{remover - count_page}:{category_id}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, number_of_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_nextp:{remover + count_page}:{category_id}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_to_category"))
    return keyboard


# Следующая страница формул для их изменения
def position_edit_next_page_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_formulas = get_formulasx("*", category_id=category_id)
    for a in range(remover, len(get_formulas)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_formulas[a][2]} | {get_formulas[a][3]}",
                                              callback_data=f"position_edit:{get_formulas[a][1]}:{remover}:{category_id}"))
        x += 1
    if remover + count_page >= len(get_formulas):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_prevp:{remover - count_page}:{category_id}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, number_of_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_nextp:{remover + count_page}:{category_id}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_to_category"))
    return keyboard


# Предыдущая страница формул для их изменения
def position_edit_previous_page_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_formulas = get_formulasx("*", category_id=category_id)
    for a in range(remover, len(get_formulas)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_formulas[a][2]} | {get_formulas[a][3]}",
                                              callback_data=f"position_edit:{get_formulas[a][1]}:{remover}:{category_id}"))
        x += 1
    if remover <= 0:
        number_of_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_nextp:{remover + count_page}:{category_id}")
        keyboard.add(number_of_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"edit_position_nextp:{remover + count_page}:{category_id}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"edit_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_to_category"))
    return keyboard


################################################################################################
################################## СТРАНИЦЫ ПРОСМОТРА ФОРМУЛ #################################
# Стартовые страницы категорий при просмотре формул
def show_formula_open_category_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(text=f"{get_categories[a][2]}",
                                              callback_data=f"buy_open_category:{get_categories[a][1]}"))
        x += 1
    if len(get_categories) <= 10:
        pass
    elif len(get_categories) > count_page and remover < 10:
        number_of_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_category_nextp:{remover + count_page}")
        keyboard.add(number_of_kb, next_kb)
    elif remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_category_prevp:{remover - count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, number_of_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_category_nextp:{remover + count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    return keyboard


# Следующая страница категорий при просмотре формул
def show_formula_next_page_category_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"buy_open_category:{get_categories[a][1]}"))
        x += 1
    if remover + count_page >= len(get_categories):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_category_prevp:{remover - count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, number_of_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_category_nextp:{remover + count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    return keyboard


# Предыдущая страница категорий при просмотре формул
def show_formula_previous_page_category_ap(remover):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_categories = get_all_categoriesx()
    for a in range(remover, len(get_categories)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_categories[a][2]}",
                                              callback_data=f"buy_open_category:{get_categories[a][1]}"))
        x += 1
    if remover <= 0:
        number_of_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_category_nextp:{remover + count_page}")
        keyboard.add(number_of_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_category_nextp:{remover + count_page}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_category_prevp:{remover - count_page}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    return keyboard


########################################### ФОРМУЛЫ ##########################################
# Стартовые страницы формул
def show_formula_item_position_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_formulas = get_formulasx("*", category_id=category_id)
    for a in range(remover, len(get_formulas)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_formulas[a][2]} | {get_formulas[a][3]}",
                                              callback_data=f"buy_open_position:{get_formulas[a][1]}:{remover}:{category_id}"))
        x += 1
    if len(get_formulas) <= 10:
        pass
    elif len(get_formulas) > count_page and remover < 10:
        number_of_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_position_nextp:{remover + count_page}:{category_id}")
        keyboard.add(number_of_kb, next_kb)
    elif remover + count_page >= len(get_formulas):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_position_prevp:{remover - count_page}:{category_id}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, number_of_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_position_nextp:{remover + count_page}:{category_id}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_show_formula_to_category"))
    return keyboard


# Следующая страница формул
def item_buy_next_page_position_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_formulas = get_formulasx("*", category_id=category_id)
    for a in range(remover, len(get_formulas)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_formulas[a][2]} | {get_formulas[a][3]}",
                                              callback_data=f"buy_open_position:{get_formulas[a][1]}:{remover}:{category_id}"))
        x += 1
    if remover + count_page >= len(get_formulas):
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_position_prevp:{remover - count_page}:{category_id}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        keyboard.add(prev_kb, number_of_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_position_nextp:{remover + count_page}:{category_id}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_show_formula_to_category"))
    return keyboard


# Предыдущая страница формул
def item_buy_previous_page_position_ap(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_formulas = get_formulasx("*", category_id=category_id)
    for a in range(remover, len(get_formulas)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_formulas[a][2]} | {get_formulas[a][3]}",
                                              callback_data=f"buy_open_position:{get_formulas[a][1]}:{remover}:{category_id}"))
        x += 1
    if remover <= 0:
        number_of_kb = InlineKeyboardButton("🔸 1 🔸", callback_data="...")
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_position_nextp:{remover + count_page}:{category_id}")
        keyboard.add(number_of_kb, next_kb)
    else:
        next_kb = InlineKeyboardButton("➡ Далее ➡",
                                       callback_data=f"buy_position_nextp:{remover + count_page}:{category_id}")
        number_of_kb = InlineKeyboardButton(f"🔸 {str(remover + count_page)[:-1]} 🔸", callback_data="...")
        prev_kb = InlineKeyboardButton("⬅ Назад ⬅",
                                       callback_data=f"buy_position_prevp:{remover - count_page}:{category_id}")
        keyboard.add(prev_kb, number_of_kb, next_kb)
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_show_formula_to_category"))
    return keyboard


def print_formula(remover, category_id):
    x = 0
    keyboard = InlineKeyboardMarkup()
    get_formulas = get_formulasx("*", category_id=category_id)
    for a in range(remover, len(get_formulas)):
        if x < count_page:
            keyboard.add(InlineKeyboardButton(f"{get_formulas[a][2]} | {get_formulas[a][3]}",
                                              callback_data=f"buy_open_position:{get_formulas[a][1]}:{remover}:{a}"))
        x += 1
    keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩",
                                      callback_data=f"back_show_formula_to_category"))
    return keyboard
