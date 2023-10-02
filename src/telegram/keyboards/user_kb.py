from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from fluentogram import TranslatorRunner

def requert_number(l10n: TranslatorRunner):
    req_btn = KeyboardButton(
        text=l10n.request.contact(),
        request_contact=True
    )
    markup = ReplyKeyboardMarkup(
        keyboard=[[req_btn]],
        resize_keyboard=True,
        one_time_keyboard=True)
    return markup