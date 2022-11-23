from aiogram import Dispatcher

from .all_filters import IsPrivate, IsAdmin, IsUser


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
