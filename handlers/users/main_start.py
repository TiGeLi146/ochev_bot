from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import IsUser
from keyboards.default import check_user_out_func
from loader import dp, bot
from utils.db_api.sqlite import *
from utils.other_func import clear_firstname


# Обработка кнопки "На главную" и команды "/start"
@dp.message_handler(text="⬅ На главную", state="*")
@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    first_name = clear_firstname(message.from_user.first_name)
    get_user_id = get_userx(user_id=message.from_user.id)
    if get_user_id is None:
        add_userx(message.from_user.id, message.from_user.username)
    # else:
    #     if message.from_user.username is not None:
    #         if message.from_user.username.lower() != get_user_id[2]:
    #             update_userx(get_user_id[1], user_login=message.from_user.username.lower())

    await message.answer("<b>Бот готов к использованию.</b>\n"
                         "Если не появились вспомогательные кнопки\n"
                         "Введите /start",
                         reply_markup=check_user_out_func(message.from_user.id))


@dp.message_handler(IsUser(), state="*")
@dp.callback_query_handler(IsUser(), state="*")
async def send_user_message(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id,
                           "<b>Ваш профиль не был найден.</b>\n"
                           "Введите /start")
