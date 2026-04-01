from telegram import Update
from telegram.ext import ContextTypes
from ..keyboards.main_menu import main_menu
from ..services.user_service import get_user_settings
from ..services.translation_service import get_text

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_settings = get_user_settings(update.effective_user.id)
    ui_lang = user_settings.get("ui_lang", "en")
    
    welcome_text = get_text('welcome', ui_lang)
    
    # Check if triggered by command or button
    if update.message:
        await update.message.reply_text(
            welcome_text,
            reply_markup=main_menu(ui_lang)
        )
    elif update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.message.reply_text(
            welcome_text,
            reply_markup=main_menu(ui_lang)
        )