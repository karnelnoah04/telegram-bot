from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot aktif 24 jam 🚀")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_webhook(
    listen="0.0.0.0",
    port=int(os.getenv("PORT", 8080)),
    webhook_url=os.getenv("WEBHOOK_URL")
)
