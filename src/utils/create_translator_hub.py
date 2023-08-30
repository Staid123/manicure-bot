from fluentogram import TranslatorHub, FluentTranslator
from fluent_compiler.bundle import FluentBundle


def create_translator_hub() -> TranslatorHub:
     
    return TranslatorHub(
        {'ru':'ru'},
        [
            FluentTranslator(
                    'ru', FluentBundle.from_files(
                        'ru_RU',
                        filenames=[
                            'locales/ru-Ru/txt.ftl'
                        ]
                    )
            )
        ],
        root_locale='ru'
    )