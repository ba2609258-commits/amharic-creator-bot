import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters


TOKEN = os.environ["BOT_TOKEN"]


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

    def log_message(self, format, *args):
        pass


def run_health_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ሰላም! 🤖🔥\n\n"
        "እኔ Amharic Creator AI ነኝ።\n"
        "በቅርቡ YouTube ይዘት እንድትፈጥር እረዳሃለሁ። 🎬\n\n"
        "Topic ላክልኝ!"
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(
        f"ተቀብያለሁ! ✅\n\n"
        f"Topic: {text}\n\n"
        "AI YouTube Creator በቅርቡ ይሰራል። 🔥"
    )


def main():
    threading.Thread(target=run_health_server, daemon=True).start()

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message)
    )

    application.run_polling()


if __name__ == "__main__":
    main()
