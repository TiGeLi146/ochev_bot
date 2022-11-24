from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from filters import IsAdmin
from keyboards.default import items_default
from keyboards.inline import *
from keyboards.inline.formula_page import *
from loader import dp, bot
from states.state_admin_func import StoragePosition, StorageCategory


# Создание новой категории
@dp.message_handler(IsAdmin(), text="Создать категорию", state="*")
async def category_create_new(message: types.Message, state: FSMContext):
    await state.finish()
    await StorageCategory.here_input_category_name.set()
    await message.answer("<b>Введите название для категории</b>")


# Открытие страниц выбора категорий для редактирования
@dp.message_handler(IsAdmin(), text="Изменить категорию", state="*")
async def category_open_edit(message: types.Message, state: FSMContext):
    await state.finish()
    get_categories = get_all_categoriesx()
    if len(get_categories) >= 1:
        get_kb = category_open_edit_ap(0)
        await message.answer("<b>Выберите категорию для изменения</b>", reply_markup=get_kb)
    else:
        await message.answer("<b>Категории отсутствуют</b>")


# Окно с уточнением удалить все категории (позиции и товары включительно)
@dp.message_handler(IsAdmin(), text="Удалить категории", state="*")
async def category_remove_all(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b>Вы действительно хотите удалить все категории?</b>\n"
                         "Также, будут удалены все формулы",
                         reply_markup=confirm_clear_category_inl)


# Создание новой формулы
@dp.message_handler(IsAdmin(), text="Добавить формулу", state="*")
async def position_create_new(message: types.Message, state: FSMContext):
    await state.finish()
    get_categories = get_all_categoriesx()
    if len(get_categories) >= 1:
        get_kb = position_open_create_ap(0)
        await message.answer("<b>Выберите категорию для формулы</b>", reply_markup=get_kb)
    else:
        await message.answer("<b>Отсутствуют категории для создания формулы.</b>")


# Начальные категории для изменения формулы
@dp.message_handler(IsAdmin(), text="Изменить формулу", state="*")
async def choice_category_for_edit_position(message: types.Message, state: FSMContext):
    await state.finish()
    get_kb = position_open_edit_category_ap(0)
    await message.answer("<b>Выберите категорию с нужной вам формулой</b>", reply_markup=get_kb)


# Подтверждение удаления всех формул
@dp.message_handler(IsAdmin(), text="Удалить формулы", state="*")
async def open_create_position(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b>Вы действительно хотите удалить все формулы?</b>",
                         reply_markup=confirm_clear_position_inl)


################################################################################################
####################################### СОЗДАНИЕ КАТЕГОРИЙ #####################################
# Принятие названия категории для её создания
@dp.message_handler(IsAdmin(), state=StorageCategory.here_input_category_name)
async def category_create_input_name(message: types.Message, state: FSMContext):
    category_id = [random.randint(100000000, 999999999)]
    add_categoryx(category_id[0], message.text)
    await state.finish()
    await message.answer("<b>Категория была успешно создана</b>",
                         reply_markup=items_default)


################################################################################################
####################################### ИЗМЕНЕНИЕ КАТЕГОРИЙ ####################################
# Следующая страница выбора категорий для редактирования
@dp.callback_query_handler(IsAdmin(), text_startswith="edit_catategory_nextp", state="*")
async def category_edit_next_page(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])

    get_kb = category_edit_next_page_ap(remover)
    await bot.edit_message_text("<b>Выберите категорию для изменения</b>",
                                call.from_user.id,
                                call.message.message_id,
                                reply_markup=get_kb)


# Предыдущая страница выбора категорий для редактирования
@dp.callback_query_handler(IsAdmin(), text_startswith="edit_catategory_prevp", state="*")
async def category_edit_prev_page(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])

    get_kb = category_edit_prev_page_ap(remover)
    await bot.edit_message_text("<b>Выберите категорию для изменения</b>",
                                call.from_user.id,
                                call.message.message_id,
                                reply_markup=get_kb)


# Выбор текущей категории для редактирования
@dp.callback_query_handler(IsAdmin(), text_startswith="edit_category_here", state="*")
async def category_open_for_edit(call: CallbackQuery, state: FSMContext):
    category_id = int(call.data.split(":")[1])
    remover = int(call.data.split(":")[2])

    messages, keyboard = edit_category_func(category_id, remover)
    await bot.edit_message_text(messages,
                                call.from_user.id,
                                call.message.message_id,
                                reply_markup=keyboard)


# Возвращение к списку выбора категорий для редактирования
@dp.callback_query_handler(IsAdmin(), text_startswith="back_category_edit", state="*")
async def category_back_for_edit(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])

    get_kb = category_open_edit_ap(remover)
    await bot.edit_message_text("<b>Выберите категорию для изменения</b>",
                                call.from_user.id,
                                call.message.message_id,
                                reply_markup=get_kb)


######################################## САМО ИЗМЕНЕНИЕ КАТЕГОРИИ ########################################
# Изменение названия категории
@dp.callback_query_handler(IsAdmin(), text_startswith="category_edit_name", state="*")
async def category_edit_name(call: CallbackQuery, state: FSMContext):
    category_id = int(call.data.split(":")[1])
    remover = int(call.data.split(":")[2])
    async with state.proxy() as data:
        data["here_cache_category_id"] = category_id
        data["here_cache_category_remover"] = remover
    await StorageCategory.here_change_category_name.set()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id,
                           "<b>Введите новое название для категории:</b>")


# Принятие нового имени для категории
@dp.message_handler(IsAdmin(), state=StorageCategory.here_change_category_name)
async def category_name_was_changed(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        category_id = data["here_cache_category_id"]
        remover = data["here_cache_category_remover"]
    update_categoryx(category_id, category_name=message.text)
    await state.finish()
    await message.answer("<b>Название было успешно изменено</b>",
                         reply_markup=items_default)
    messages, keyboard = edit_category_func(category_id, remover)
    await message.answer(messages, reply_markup=keyboard)


# Окно с уточнением удалить категорию
@dp.callback_query_handler(IsAdmin(), text_startswith="category_remove", state="*")
async def category_remove(call: CallbackQuery, state: FSMContext):
    category_id = int(call.data.split(":")[1])
    remover = int(call.data.split(":")[2])
    await bot.edit_message_text("<b>Вы действительно хотите удалить категорию и все её данные?</b>",
                                call.from_user.id,
                                call.message.message_id,
                                reply_markup=confirm_remove_func(category_id, remover))


# Отмена удаления категории
@dp.callback_query_handler(IsAdmin(), text_startswith="not_remove_category", state="*")
async def category_remove_cancel(call: CallbackQuery, state: FSMContext):
    category_id = int(call.data.split(":")[1])
    remover = int(call.data.split(":")[2])
    messages, keyboard = edit_category_func(category_id, remover)
    await bot.edit_message_text(messages,
                                call.from_user.id,
                                call.message.message_id,
                                reply_markup=keyboard)


# Согласие на удаление категории
@dp.callback_query_handler(IsAdmin(), text_startswith="yes_remove_category", state="*")
async def category_remove_confirm(call: CallbackQuery, state: FSMContext):
    category_id = int(call.data.split(":")[1])
    remover = int(call.data.split(":")[2])

    remove_categoryx(category_id=category_id)  # Удаление всех категорий
    remove_positionx(category_id=category_id)  # Удаление всех позиций

    await bot.edit_message_text("<b>Категория и все её данные были успешно удалены</b>",
                                call.from_user.id,
                                call.message.message_id)
    get_kb = category_open_edit_ap(remover)
    await bot.send_message(call.from_user.id,
                           "<b>Выберите категорию для изменения</b>",
                           reply_markup=get_kb)


################################################################################################
#################################### УДАЛЕНИЕ ВСЕХ КАТЕГОРИЙ ###################################
# Согласие на удаление всех категорий
@dp.callback_query_handler(IsAdmin(), text_startswith="confirm_clear_category", state="*")
async def category_remove_all_confirm(call: CallbackQuery, state: FSMContext):
    clear_categoryx()
    clear_positionx()
    await bot.edit_message_text("<b>Вы успешно удалили все категории и формулы</b>",
                                call.from_user.id,
                                call.message.message_id)


# Отмена удаления всех категорий
@dp.callback_query_handler(IsAdmin(), text_startswith="cancel_clear_category", state="*")
async def category_remove_all_cancel(call: CallbackQuery, state: FSMContext):
    await bot.edit_message_text("<b>Вы отменили удаление всех категорий ☑</b>",
                                call.from_user.id,
                                call.message.message_id)


################################################################################################
####################################### ДОБАВЛЕНИЕ ФОРМУЛ #####################################
# Следующая страница выбора категорий для создания формул
@dp.callback_query_handler(IsAdmin(), text_startswith="create_position_nextp", state="*")
async def position_next_page(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])

    get_kb = position_create_next_page_ap(remover)
    await bot.edit_message_text("<b>Выберите место для формулы</b>",
                                call.from_user.id,
                                call.message.message_id,
                                reply_markup=get_kb)


# Предыдущая страница выбора категорий для создания формул
@dp.callback_query_handler(IsAdmin(), text_startswith="create_position_prevp", state="*")
async def position_prev_page(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])

    get_kb = position_create_previous_page_ap(remover)
    await bot.edit_message_text("<b>Выберите место для формулы</b>",
                                call.from_user.id,
                                call.message.message_id,
                                reply_markup=get_kb)


# Выбор категории для создания формулы
@dp.callback_query_handler(IsAdmin(), text_startswith="create_position_here", state="*")
async def position_select_category_for_create(call: CallbackQuery, state: FSMContext):
    category_id = int(call.data.split(":")[1])
    async with state.proxy() as data:
        data["here_cache_change_category_id"] = category_id
    await StoragePosition.here_input_position_name.set()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id,
                           "<b>Введите название для формулы</b>")


# Принятие названия формулы
@dp.message_handler(IsAdmin(), state=StoragePosition.here_input_position_name)
async def position_input_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["here_input_position_name"] = message.text
    await StoragePosition.here_input_position_price.set()
    await message.answer("<b>Введите формулу</b>")


# Принятие формулы
@dp.message_handler(IsAdmin(), state=StoragePosition.here_input_position_price)
async def position_input_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["here_input_position_price"] = message.text
    await StoragePosition.here_input_position_discription.set()
    async with state.proxy() as data:
        position_name = data["here_input_position_name"]
        position_price = data["here_input_position_price"]
        category_id = data["here_cache_change_category_id"]
    await state.finish()
    position_id = [random.randint(100000000, 999999999)]
    add_positionx(position_id[0], position_name, position_price, category_id)
    await message.answer("<b>Формула была успешно создана</b>",
                         reply_markup=items_default)


################################################################################################
####################################### ИЗМЕНЕНИЕ ФОРМУЛ #####################################
# Возвращение к начальным категориям для изменения формулы
@dp.callback_query_handler(IsAdmin(), text_startswith="back_to_category", state="*")
async def back_to_all_categories_for_edit_position(call: CallbackQuery, state: FSMContext):
    get_kb = position_open_edit_category_ap(0)

    await bot.edit_message_text("<b>Выберите категорию с нужной вам формулой</b>",
                                call.from_user.id,
                                call.message.message_id,
                                reply_markup=get_kb)


# Следующая страница выбора категории с формулой для редактирования
@dp.callback_query_handler(IsAdmin(), text_startswith="edit_position_category_nextp", state="*")
async def next_page_category_for_edit_position(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])

    get_kb = position_edit_next_page_category_ap(remover)
    await bot.edit_message_text("<b>Выберите категорию с нужной вам формулой</b>",
                                call.from_user.id,
                                call.message.message_id,
                                reply_markup=get_kb)


# Предыдущая страница выбора категории с формулой для редактирования
@dp.callback_query_handler(IsAdmin(), text_startswith="edit_position_category_prevp", state="*")
async def previous_page_category_for_edit_position(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])

    get_kb = position_edit_previous_page_category_ap(remover)
    await bot.edit_message_text("<b>Выберите категорию с нужной вам формулой</b>",
                                call.from_user.id,
                                call.message.message_id,
                                reply_markup=get_kb)


# Выбор категории с нужной формулой
@dp.callback_query_handler(IsAdmin(), text_startswith="position_edit_category", state="*")
async def open_category_for_edit_position(call: CallbackQuery, state: FSMContext):
    category_id = int(call.data.split(":")[1])

    get_positions = get_positionsx("*", category_id=category_id)
    if len(get_positions) >= 1:
        get_kb = position_open_edit_ap(0, category_id)
        await bot.edit_message_text("<b>Выберите нужную вам формулу</b>",
                                    call.from_user.id,
                                    call.message.message_id,
                                    reply_markup=get_kb)
    else:
        await bot.answer_callback_query(call.id, "Формулы в данной категории отсутствуют")


# Следующая страница формул для их изменения
@dp.callback_query_handler(IsAdmin(), text_startswith="edit_position_nextp", state="*")
async def next_page_for_edit_position(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])

    get_kb = position_edit_next_page_ap(remover, category_id)
    await bot.edit_message_text("<b>Выберите категорию с нужной вам формулой</b>",
                                call.from_user.id,
                                call.message.message_id,
                                reply_markup=get_kb)


# Предыдущая страница формул для их изменения
@dp.callback_query_handler(IsAdmin(), text_startswith="edit_position_prevp", state="*")
async def previous_page_for_edit_position(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])

    get_kb = position_edit_previous_page_ap(remover, category_id)
    await bot.edit_message_text("<b>Выберите категорию с нужной вам формулой</b>",
                                call.from_user.id,
                                call.message.message_id,
                                reply_markup=get_kb)


# Выбор формулы для редактирования
@dp.callback_query_handler(IsAdmin(), text_startswith="position_edit", state="*")
async def open_for_edit_position(call: CallbackQuery, state: FSMContext):
    position_id = int(call.data.split(":")[1])
    remover = int(call.data.split(":")[2])
    category_id = int(call.data.split(":")[3])
    get_position = get_positionx("*", position_id=position_id)
    messages, keyboard, have_photo = open_edit_position_func(position_id, category_id, remover)

    if have_photo:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_photo(call.from_user.id, get_position[5], messages, reply_markup=keyboard)
    else:
        await bot.edit_message_text(messages,
                                    call.from_user.id,
                                    call.message.message_id,
                                    reply_markup=keyboard)


# Возвращение к выбору формулы для изменения
@dp.callback_query_handler(IsAdmin(), text_startswith="back_position_edit", state="*")
async def back_to_all_categories_for_choice_edit(call: CallbackQuery, state: FSMContext):
    category_id = int(call.data.split(":")[1])
    remover = int(call.data.split(":")[2])

    get_positions = get_positionsx("*", category_id=category_id)
    if len(get_positions) >= 1:
        get_kb = position_open_edit_ap(remover, category_id)
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_message(call.from_user.id,
                               "<b>Выберите нужную вам формулу</b>",
                               reply_markup=get_kb)
    else:
        await bot.edit_message_text("<b>Формулы в данной категории отсутствуют</b>",
                                    call.from_user.id,
                                    call.message.message_id)


######################################## САМО ИЗМЕНЕНИЕ ФОРМУЛЫ ########################################
# Изменение названия формулы
@dp.callback_query_handler(IsAdmin(), text_startswith="position_change_name", state="*")
async def change_position_name(call: CallbackQuery, state: FSMContext):
    category_id = int(call.data.split(":")[1])
    position_id = int(call.data.split(":")[2])
    remover = int(call.data.split(":")[3])
    async with state.proxy() as data:
        data["here_cache_category_id"] = category_id
        data["here_cache_position_id"] = position_id
        data["here_cache_position_remover"] = remover
    await StoragePosition.here_change_position_name.set()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id,
                           "<b>Введите новое название для формулы</b>")


# Принятие названия формулы для её изменения
@dp.message_handler(IsAdmin(), state=StoragePosition.here_change_position_name)
async def input_new_position_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        position_id = data["here_cache_category_id"]
        category_id = data["here_cache_position_id"]
        remover = data["here_cache_position_remover"]
    update_positionx(position_id, position_name=message.text)

    messages, keyboard, have_photo = open_edit_position_func(position_id, category_id, remover)
    await message.answer("<b>Название формулы было успешно изменено</b>", reply_markup=items_default)
    await state.finish()

    get_position = get_positionx("*", position_id=position_id)
    await bot.delete_message(message.from_user.id, message.message_id)
    if have_photo:
        await message.answer_photo(get_position[5], messages, reply_markup=keyboard)
    else:
        await message.answer(messages, reply_markup=keyboard)


# Изменение формулы
@dp.callback_query_handler(IsAdmin(), text_startswith="position_change_price", state="*")
async def change_position_price(call: CallbackQuery, state: FSMContext):
    category_id = int(call.data.split(":")[1])
    position_id = int(call.data.split(":")[2])
    remover = int(call.data.split(":")[3])
    async with state.proxy() as data:
        data["here_cache_category_id"] = category_id
        data["here_cache_position_id"] = position_id
        data["here_cache_position_remover"] = remover
    await StoragePosition.here_change_position_price.set()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id,
                           "<b>Введите новую формулу</b>")


# Принятие формулы
@dp.message_handler(IsAdmin(), state=StoragePosition.here_change_position_price)
async def input_new_position_price(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            position_id = data["here_cache_category_id"]
            category_id = data["here_cache_position_id"]
            remover = data["here_cache_position_remover"]
        update_positionx(position_id, position_price=message.text)

        messages, keyboard, have_photo = open_edit_position_func(position_id, category_id, remover)
        await message.answer("<b>Формула была успешно изменена</b>", reply_markup=items_default)
        await state.finish()

        get_position = get_positionx("*", position_id=position_id)
        await bot.delete_message(message.from_user.id, message.message_id)
        if have_photo:
            await message.answer_photo(get_position[5], messages, reply_markup=keyboard)
        else:
            await message.answer(messages, reply_markup=keyboard)


# Удаление формулы
@dp.callback_query_handler(IsAdmin(), text_startswith="position_remove_this", state="*")
async def open_category_for_create_position(call: CallbackQuery, state: FSMContext):
    position_id = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])
    remover = int(call.data.split(":")[3])

    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id,
                           "<b>Вы действительно хотите удалить формулу?</b>",
                           reply_markup=confirm_remove_position_func(position_id, category_id, remover))


# Согласие удаления формулы
@dp.callback_query_handler(IsAdmin(), text_startswith="yes_remove_position", state="*")
async def open_category_for_create_position(call: CallbackQuery, state: FSMContext):
    position_id = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])
    remover = int(call.data.split(":")[3])

    remove_positionx(position_id=position_id)
    await bot.edit_message_text("<b>Вы успешно удалили формулу</b>",
                                call.from_user.id,
                                call.message.message_id)

    get_positions = get_positionsx("*", category_id=category_id)
    if len(get_positions) >= 1:
        get_kb = position_open_edit_ap(remover, category_id)
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_message(call.from_user.id,
                               "<b>Выберите нужную вам формулу</b>",
                               reply_markup=get_kb)


# Отмена удаления формулы
@dp.callback_query_handler(IsAdmin(), text_startswith="not_remove_position", state="*")
async def open_category_for_create_position(call: CallbackQuery, state: FSMContext):
    position_id = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])
    remover = int(call.data.split(":")[3])

    messages, keyboard, have_photo = open_edit_position_func(position_id, category_id, remover)
    await state.finish()

    get_position = get_positionx("*", position_id=position_id)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    if have_photo:
        await bot.send_photo(call.from_user.id, get_position[5], messages, reply_markup=keyboard)
    else:
        await bot.send_message(call.from_user.id, messages, reply_markup=keyboard)


################################################################################################
###################################### УДАЛЕНИЕ ВСЕХ ФОРМУЛ ###################################
# Согласие на удаление всех формул
@dp.callback_query_handler(IsAdmin(), text_startswith="confirm_clear_position", state="*")
async def create_input_position_name(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    delete_msg = await bot.send_message(call.from_user.id, "<b>Ждите, формулы удаляются...</b>")
    get_positions = len(get_all_positionsx())

    clear_positionx()
    await bot.edit_message_text(f"<b>Вы успешно удалили все формулы({get_positions}шт)</b>",
                                call.from_user.id,
                                delete_msg.message_id)


# Отмена удаления формул
@dp.callback_query_handler(IsAdmin(), text_startswith="cancel_clear_position", state="*")
async def create_input_position_name(call: CallbackQuery, state: FSMContext):
    await bot.edit_message_text("<b>Вы отменили удаление всех формул</b>",
                                call.from_user.id,
                                call.message.message_id)
