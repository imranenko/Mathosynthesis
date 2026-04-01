from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackQueryHandler

from mathosynthesis.handlers import files_handler
from ..services.mathosynthesis_adapter import get_setups, generate_pdf, get_flat_setups, format_setups_text
from ..services.user_service import get_user_settings
from ..services.translation_service import get_text

WAIT_FOR_NUMBER_STATE = 1

def get_effective_message(update: Update):
    """Retrieve the original message object regardless of whether it's a callback or text."""
    if update.callback_query:
        return update.callback_query.message
    return update.message

async def start_generate(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    user_settings = get_user_settings(update.effective_user.id)
    ui_lang = user_settings.get("ui_lang", "en")

    if update.callback_query:
        await update.callback_query.answer()

    setups_dict = get_setups()
    if not setups_dict:
        message = get_effective_message(update)
        await message.reply_text(get_text('no_setups', ui_lang))
        return ConversationHandler.END

    flat_setups = get_flat_setups(setups_dict)
    setups_text = format_setups_text(setups_dict, ui_lang)
    
    context.user_data["flat_setups"] = flat_setups
    
    message = get_effective_message(update)
    await message.reply_text(setups_text, parse_mode='HTML')
    await message.reply_text(get_text('choose_setup', ui_lang))
    return WAIT_FOR_NUMBER_STATE

def get_setup_info(context: ContextTypes.DEFAULT_TYPE, index: int) -> tuple[str | None, str | None]:
    """Retrieve category and filename from the context's flat_setups."""
    setups = context.user_data.get("flat_setups", [])
    if 0 <= index < len(setups):
        return setups[index]
    return None, None

async def generate_and_send_pdf(update: Update, setup_name: str, setup_path: str):
    """Generate the PDF and send it to the user based on their settings."""
    user_settings = get_user_settings(update.effective_user.id)
    file_lang = user_settings.get("file_lang", "en")
    ui_lang = user_settings.get("ui_lang", "en")

    await update.message.reply_text(
        get_text('generating_pdf', ui_lang, name=setup_name, lang=file_lang.upper())
    )

    file_path = generate_pdf(setup_path, language=file_lang)
    
    if file_path:
        with open(file_path, "rb") as pdf_file:
            await update.message.reply_document(pdf_file)
    else:
        await update.message.reply_text(get_text('failed_pdf', ui_lang))

async def receive_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_settings = get_user_settings(update.effective_user.id)
    ui_lang = user_settings.get("ui_lang", "en")
    
    text = update.message.text.strip()

    if not text.isdigit():
        await update.message.reply_text(get_text('enter_number', ui_lang))
        return WAIT_FOR_NUMBER_STATE

    index = int(text) - 1
    category, filename = get_setup_info(context, index)

    if not filename:
        await update.message.reply_text(get_text('invalid_number', ui_lang))
        return WAIT_FOR_NUMBER_STATE

    full_path = files_handler.get_setup_path_by_name(filename)
    await generate_and_send_pdf(update, filename, full_path)
    
    return ConversationHandler.END

async def cancel_generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_settings = get_user_settings(update.effective_user.id)
    ui_lang = user_settings.get("ui_lang", "en")

    if update.callback_query:
        await update.callback_query.answer()
    
    message = get_effective_message(update)
    await message.reply_text(get_text('cancelled', ui_lang))
    return ConversationHandler.END

# ConversationHandler setup
generate_conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler("generate", start_generate),
        CallbackQueryHandler(start_generate, pattern="^generate$")
    ],
    states={
        WAIT_FOR_NUMBER_STATE: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, receive_number)
        ]
    },
    fallbacks=[CommandHandler("cancel", cancel_generate)],
    per_message=False,
)

