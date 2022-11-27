from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.formula_page import *
from loader import dp


# Разбив сообщения на несколько, чтобы не прилетало ограничение от ТГ
def split_messages(get_list, count):
    return [get_list[i:i + count] for i in range(0, len(get_list), count)]


# Обработка кнопки "Смотреть формулы"
@dp.message_handler(text="Смотреть формулы", state="*")
async def show_search(message: types.Message, state: FSMContext):
    await state.finish()
    get_categories = get_all_categoriesx()
    if len(get_categories) >= 1:
        get_kb = show_formula_open_category_ap(0)
        await message.answer("<b>Выберите нужный предмет:</b>", reply_markup=get_kb)
    else:
        await message.answer("<b>Формулы в данное время отсутствуют.</b>")


################################################################################################
######################################### ПРОСМОТР ФОРМУЛ #######################################
# Открытие категории для просмотра
@dp.callback_query_handler(text_startswith="buy_open_category", state="*")
async def open_category_for_show_formula(call: CallbackQuery, state: FSMContext):
    category_id = int(call.data.split(":")[1])
    get_category = get_categoryx("*", category_id=category_id)
    get_formulas = get_formulasx("*", category_id=category_id)

    get_kb = show_formula_item_position_ap(0, category_id)
    if len(get_formulas) >= 1:
        await call.message.edit_text("<b>Выберите формулу:</b>",
                                     reply_markup=get_kb)
    else:
        await call.answer(f"Формулы в категории {get_category[2]} отсутствуют.")


# Вернуться к предыдущей категории при просмотре
@dp.callback_query_handler(text_startswith="back_show_formula_to_category", state="*")
async def back_category_for_show_formula(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("<b>Выберите нужный предмет:</b>",
                                 reply_markup=show_formula_open_category_ap(0))


# Следующая страница категорий при просмотре
@dp.callback_query_handler(text_startswith="buy_category_nextp", state="*")
async def show_formula_next_page_category(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])

    await call.message.edit_text("<b>Выберите нужный предмет:</b>",
                                 reply_markup=show_formula_next_page_category_ap(remover))


# Предыдущая страница категорий при просмотре
@dp.callback_query_handler(text_startswith="buy_category_prevp", state="*")
async def show_formula_prev_page_category(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])

    await call.message.edit_text("<b>Выберите нужный предмет:</b>",
                                 reply_markup=show_formula_previous_page_category_ap(remover))


# Следующая страница формул
@dp.callback_query_handler(text_startswith="buy_position_nextp", state="*")
async def show_formula_next_page_position(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])

    await call.message.edit_text("<b>Выберите нужную формулу:</b>",
                                 reply_markup=item_buy_next_page_position_ap(remover, category_id))


# Предыдущая страница формул
@dp.callback_query_handler(text_startswith="buy_position_prevp", state="*")
async def show_formula_prev_page_position(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])

    await call.message.edit_text("<b>Выберите нужную формулу:</b>",
                                 reply_markup=item_buy_previous_page_position_ap(remover, category_id))


# Возвращение к страницам формул
@dp.callback_query_handler(text_startswith="back_show_formula_position", state="*")
async def show_formula_next_page_position(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])

    await call.message.delete()
    await call.message.answer("<b>Выберите нужную формулу:</b>",
                              reply_markup=show_formula_item_position_ap(remover, category_id))


# Отправление формулы отдельным сообщением
@dp.callback_query_handler(text_startswith="buy_open_position", state="*")
async def show_formula_next_page_position(call: CallbackQuery, state: FSMContext):
    position_id = int(call.data.split(":")[1])
    remover = int(call.data.split(":")[2])
    category_id = int(call.data.split(":")[3])

    print(call.data)

    get_formulas = get_positionx("*", category_id=category_id, position_id=position_id)

    await call.message.edit_text(f"{get_formulas[2]} | {get_formulas[3]}",
                                 reply_markup=print_formula(remover, category_id))
