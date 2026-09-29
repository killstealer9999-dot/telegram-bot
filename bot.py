from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8876515706:AAEj8R1ZWkjO9iYbnYl-W1K6jQaUwQSl3fQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot aktif! 🤖")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot sedang berjalan...")
app.run_polling()