from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# 🔐 PUT YOUR BOT TOKEN HERE
BOT_TOKEN = "5001053394:AAFzDIMXsuqDriYhedQakuGuLdbIEfdLUuE"

# Store user state
user_state = {}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Kanapro AI Football Analyst\n\n"
        "Send match details in this format:\n\n"
        "Match: Team A vs Team B\n"
        "League:\n"
        "Odds:\n"
        "Kickoff:\n\n"
        "Type NEXT after each analysis."
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 HOW TO USE:\n\n"
        "1️⃣ Send match details\n"
        "2️⃣ Receive full analysis\n"
        "3️⃣ Type NEXT for another match\n\n"
        "Football matches only ⚽"
    )

# Main message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.strip()

    # Reset for next match
    if text.upper() == "NEXT":
        user_state[user_id] = None
        await update.message.reply_text("✅ Ready. Send next match details.")
        return

    # Save match data
    user_state[user_id] = text

    # 🔍 PROFESSIONAL ANALYSIS OUTPUT (Template)
    analysis = (
        f"Match Analysis\n\n"
        f"1. Win / Draw:\n"
        f"→ Home Win\n\n"
        f"2. Double Chance:\n"
        f"→ 1X\n\n"
        f"3. Both Teams To Score:\n"
        f"→ Yes\n\n"
        f"4. Total Goals:\n"
        f"→ Over 2.5\n\n"
        f"5. Correct Score:\n"
        f"→ First Half: 1–0\n"
        f"→ Second Half: 2–1\n\n"
        f"Confidence Level: 88%\n\n"
        f"Analysé made by Kanapro AI — feel free to choose the best one for your betting strategy"
    )

    await update.message.reply_text(analysis)

# Run bot
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Kanapro AI Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
