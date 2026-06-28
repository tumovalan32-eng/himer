import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = "8700117657:AAFt_g3fd0MIS6p7p6ENp_1r7LwGerDW65E"
GROQ_API_KEY = "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"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if not text:
        return
    await update.message.reply_chat_action("typing")
    res = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
        json={"model": "llama-3.3-70b-versatile", "messages": [
            {"role": "system", "content": "Тебя зовут Химера. Ты дружелюбный ИИ-ассистент. Отвечай кратко и по-русски."},
            {"role": "user", "content": text}
        ]}
    )
    await update.message.reply_text(res.json()["choices"][0]["message"]["content"])

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))
app.run_polling()
