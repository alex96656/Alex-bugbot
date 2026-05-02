from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import config
import responses as r
TOKEN = config.BOT_TOKEN
OWNER_ID = config.OWNER_ID
OWNER_NAME = config.OWNER_NAME
OWNER_USERNAME = config.OWNER_USERNAME


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = (update.message.text or "").lower()

    if not text:
        return

    # 👑 OWNER MODE
    if user.id == OWNER_ID:
        if "status" in text:
            await update.message.reply_text("👑 Bot is alive and running perfectly.")
            return

        if "test" in text:
            await update.message.reply_text("👑 Owner system active.")
            return

    # ---------------- KEYWORD SYSTEM ----------------

    # 👋 greetings
    if any(x in text for x in ["hello", "hi", "hey"]):
        await update.message.reply_text(r.pick(r.HELLO))
        return

    # 💞 love / relationship vibes
    if any(x in text for x in ["love", "crush", "loves", "relationship"]):
        await update.message.reply_text(r.pick(r.LOVE_VIBES))
        return

    # 😂 roast trigger
    if any(x in text for x in ["stupid", "lol", "bruh", "slow", "did you"]):
        await update.message.reply_text(r.pick(r.ROAST))
        return

    # 🤖 bot mention
    if "bot" in text:
        await update.message.reply_text(r.pick(r.BOT_REPLY))
        return

    # 👑 owner mention
    if "alex" in text:
        await update.message.reply_text(
            f"👑 {OWNER_NAME} ({OWNER_USERNAME}) is my creator."
        )
        return

    # 💬 default fallback
    if len(text) > 20:
        await update.message.reply_text("🎀 noted...")
    else:
        await update.message.reply_text("👀 hmm...")

import os
BOT_TOKEN = os.getenv("BOT_TOKEN")
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🔥 Noel-style bot running...")
app.run_polling()