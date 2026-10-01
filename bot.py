import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler,
    CallbackQueryHandler, ContextTypes,
)

TOKEN = os.environ["8869572085:AAFRpHjbTRGWlvWiZ808KiD-Ov5q8BrshtQ"]


def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📚 دسترسی به جزوات و منابع", callback_data="resources")],
        [InlineKeyboardButton("📤 ارسال جزوه", callback_data="send_note"),
         InlineKeyboardButton("👥 عضو تیم ما شو", callback_data="join")],
        [InlineKeyboardButton("💬 ارتباط با ما", callback_data="contact"),
         InlineKeyboardButton("🎬 درباره فراسو", callback_data="about")],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\nبه جزوه‌یار فراسو خوش اومدی 🌱",
        reply_markup=main_menu(),
    )


async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("این بخش به‌زودی اضافه می‌شه.")


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(on_button))
    app.run_polling()


if __name__ == "__main__":
    main()
