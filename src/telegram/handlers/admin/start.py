from aiogram import Router, Bot, F
from aiogram.filters import StateFilter, Command
from aiogram.types import Message, CallbackQuery
from fluentogram import TranslatorRunner
from src.telegram.keyboards import answer_yes, set_main_menu
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from src.telegram.states import FSMadmin

router = Router(name='admin/start/router')


@router.message(
        Command(commands=['add_record', 'start']),
        StateFilter(default_state)
)
async def command_start(
    message: Message, 
    l10n: TranslatorRunner, 
    bot: Bot, 
    state: FSMContext
    ) -> None:
    await message.answer(
        text=l10n.admin.hello(),
        reply_markup=answer_yes())
    await set_main_menu(bot, l10n)
    await state.set_state(state=FSMadmin.fill_yes_no_in_start)


'''@router.message(
    Command(commands=['add_record', 'start']), 
    ~StateFilter(default_state)
)
async def command_start(
    message: Message, 
    l10n: TranslatorRunner, 
    bot: Bot, 
    state: FSMContext
    ) -> None:
    await message.answer(
        text=l10n.admin.hello(),
        reply_markup=answer_yes())
    await set_main_menu(bot, l10n)
    await state.clear()'''
    


@router.callback_query(
    StateFilter(FSMadmin.fill_yes_no_in_start), 
    F.data=='no'
)
async def cancel_button(
    callback: CallbackQuery,
    state: FSMContext,
    l10n: TranslatorRunner
) -> None:
    await callback.message.delete_reply_markup()
    await callback.message.edit_text(text=l10n.admin.no())
    await state.clear()