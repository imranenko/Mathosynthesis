from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from ..services.translation_service import get_text

def settings_main_menu(lang: str = 'en'):
    """Main settings selection keyboard."""
    keyboard = [
        [InlineKeyboardButton(get_text('btn_doc_lang', lang), callback_data="select_file_lang")],
        [InlineKeyboardButton(get_text('btn_ui_lang', lang), callback_data="select_ui_lang")],
        [InlineKeyboardButton(get_text('btn_back_menu', lang), callback_data="start_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def file_language_menu(lang: str = 'en'):
    """Keyboard for selecting document (file) language."""
    keyboard = [
        [InlineKeyboardButton(get_text('lang_en', lang), callback_data="apply_file_lang_en")],
        [InlineKeyboardButton(get_text('lang_de', lang), callback_data="apply_file_lang_de")],
        [InlineKeyboardButton(get_text('lang_uk', lang), callback_data="apply_file_lang_uk")],
        [InlineKeyboardButton(get_text('btn_back_settings', lang), callback_data="settings")]
    ]
    return InlineKeyboardMarkup(keyboard)

def ui_language_menu(lang: str = 'en'):
    """Keyboard for selecting interface (UI) language."""
    keyboard = [
        [InlineKeyboardButton(get_text('lang_en', lang), callback_data="apply_ui_lang_en")],
        [InlineKeyboardButton(get_text('lang_de', lang), callback_data="apply_ui_lang_de")],
        [InlineKeyboardButton(get_text('lang_uk', lang), callback_data="apply_ui_lang_uk")],
        [InlineKeyboardButton(get_text('btn_back_settings', lang), callback_data="settings")]
    ]
    return InlineKeyboardMarkup(keyboard)

def language_applied_menu(lang: str = 'en'):
    """Simple keyboard shown after a language has been applied."""
    keyboard = [
        [InlineKeyboardButton(get_text('btn_back_settings', lang), callback_data="settings")]
    ]
    return InlineKeyboardMarkup(keyboard)
