from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import ADMINS as admins
from utils.db_api.sqlite import get_userx


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        if str(message.from_user.id) in admins:
            return True
        else:
            return False


class IsUser(BoundFilter):
    async def check(self, message: types.Message):
        get_profile = get_userx(user_id=message.from_user.id)
        if get_profile is not None:
            return False
        else:
            return True
