from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# توکن ربات
TOKEN = "8869572085:AAFRpHjbTRGWlvWiZ808KiD-Ov5q8BrshtQ"

# آیدی ادمین
ADMIN_ID = 1664573096


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n\n"
        "به جزوه‌یار فراسو خوش اومدی 🌱\n\n"
        "از منوی زیر می‌تونی بخش مورد نظرت رو انتخاب کنی."
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🤖 ربات فراسو اجرا شد...")
    app.run_polling()


if name == "__main__":
    main()
