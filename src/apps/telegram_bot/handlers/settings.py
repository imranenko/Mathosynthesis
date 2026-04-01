from telegram import Update
from telegram.ext import ContextTypes
from ..services.user_service import update_user_settings, get_user_settings
from ..services.translation_service import get_text
from ..keyboards.settings_keyboards import (
    settings_main_menu, 
    file_language_menu,
    ui_language_menu,
    language_applied_menu
)

async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Entry point for /settings or Settings button."""
    user_settings = get_user_settings(update.effective_user.id)
    ui_lang = user_settings.get("ui_lang", "en")

    if update.callback_query:
        await update.callback_query.answer()
        message = update.callback_query.message
    else:
        message = update.message

    await message.reply_text(
        get_text('settings_title', ui_lang),
        reply_markup=settings_main_menu(ui_lang)
    )

async def file_language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show document language choices."""
    user_settings = get_user_settings(update.effective_user.id)
    ui_lang = user_settings.get("ui_lang", "en")

    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        get_text('select_doc_lang', ui_lang),
        reply_markup=file_language_menu(ui_lang)
    )

async def ui_language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show interface language choices."""
    user_settings = get_user_settings(update.effective_user.id)
    ui_lang = user_settings.get("ui_lang", "en")

    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        get_text('select_ui_lang', ui_lang),
        reply_markup=ui_language_menu(ui_lang)
    )

async def apply_file_lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Apply the selected document language."""
    query = update.callback_query
    await query.answer()

    # query.data is 'apply_file_lang_en'
    lang_code = query.data.split("_")[-1]

    update_user_settings(query.from_user.id, file_lang=lang_code)
    
    user_settings = get_user_settings(query.from_user.id)
    ui_lang = user_settings.get("ui_lang", "en")

    await query.edit_message_text(
        get_text('success_doc_lang', ui_lang, lang=lang_code.upper()),
        reply_markup=language_applied_menu(ui_lang)
    )

async def apply_ui_lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Apply the selected interface language."""
    query = update.callback_query
    await query.answer()

    # query.data is 'apply_ui_lang_en'
    lang_code = query.data.split("_")[-1]

    update_user_settings(query.from_user.id, ui_lang=lang_code)

    # We need to fetch the updated ui_lang to show the success message in the new language
    await query.edit_message_text(
        get_text('success_ui_lang', lang_code, lang=lang_code.upper()),
        reply_markup=language_applied_menu(lang_code)
    )