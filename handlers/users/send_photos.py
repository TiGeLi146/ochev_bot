from aiogram.dispatcher.filters import Command

from loader import dp, bot
from aiogram.types import ContentType, Message, InputFile


@dp.message_handler(Command("get_qr"))
async def send_photo(message: Message):
    file = InputFile(path_or_bytesio="photos/qr.png")
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=file,
        caption="QR для перехода на GitHub"
    )
