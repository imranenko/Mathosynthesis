import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from .handlers.start import start
from .handlers.generate import generate_conv_handler
from .handlers.settings import (
    settings,
    file_language_selection,
    ui_language_selection,
    apply_file_lang,
    apply_ui_lang,
)

load_dotenv()

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise EnvironmentError(
        "TELEGRAM_BOT_TOKEN is not set. "
        "Copy .env.example to .env and fill in your token."
    )

app = ApplicationBuilder().token(TOKEN).build()

# --- Command Handlers ---
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("settings", settings))
# app.add_handler(CommandHandler("generate", generate))

# --- Conversation Handlers ---
app.add_handler(generate_conv_handler)

# --- Callback Query Handlers ---
# Main Menu / Start Menu
app.add_handler(CallbackQueryHandler(start, pattern="^start_menu$"))

# Settings Flow
app.add_handler(CallbackQueryHandler(settings, pattern="^settings$"))
app.add_handler(CallbackQueryHandler(file_language_selection, pattern="^select_file_lang$"))
app.add_handler(CallbackQueryHandler(ui_language_selection, pattern="^select_ui_lang$"))
app.add_handler(CallbackQueryHandler(apply_file_lang, pattern="^apply_file_lang_"))
app.add_handler(CallbackQueryHandler(apply_ui_lang, pattern="^apply_ui_lang_"))

# Start polling
if __name__ == "__main__":
    print("Bot is starting...")
    app.run_polling()