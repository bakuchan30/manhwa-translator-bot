import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Baku Manhwa Translator Bot\n\n"
        "Manga/Manhwa page bhejo.\n"
        "Abhi bot testing mode mein hai. 🔥"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 Help\n\n"
        "• /start - Bot start karo\n"
        "• /help - Help dekho\n"
        "• Manga page bhejo - translation system baad mein add hoga"
    )


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable missing")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()


if name == "main":
    main()
