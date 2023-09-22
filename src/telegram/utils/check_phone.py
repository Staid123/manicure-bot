from aiogram.types import Message
from fluentogram import TranslatorRunner


async def check_phone(message: Message, l10n: TranslatorRunner):
    if len(message.text) == 12 and message.text.startswith('380'):
        return True
    await message.answer(text=l10n.admin.bad.phone())