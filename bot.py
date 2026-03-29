from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello 😄 Bot working!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, reply))

app.run_polling()
