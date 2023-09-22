from aiogram.types import BotCommand
from aiogram import Bot
from fluentogram import TranslatorRunner


async def set_main_menu(bot: Bot, l10n: TranslatorRunner):
    main_menu_commands = [
        BotCommand(
        command=l10n.command.help(),
        description=l10n.command.help.description()
        ) 
    ]
    await bot.set_my_commands(main_menu_commands)