from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from ..services.translation_service import get_text

def main_menu(lang: str = 'en'):
    """Main menu keyboard."""
    keyboard = [
        [InlineKeyboardButton(get_text('btn_generate', lang), callback_data="generate")],
        [InlineKeyboardButton(get_text('btn_settings', lang), callback_data="settings")]
    ]
    return InlineKeyboardMarkup(keyboard)