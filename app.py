import logging
from flask import Flask  # <--- THÊM DÒNG NÀY
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# --- CẤU HÌNH ---
BOT_TOKEN = "8893681330:AAHSsMArvUSvwTXxbjDBxEzhKNW74Zb-_FE"
WEB_APP_URL = "https://xacthuckey.x10.mx/0.html"

# --- TẠO FLASK APP (THÊM PHẦN NÀY) ---
app = Flask(__name__)  # <--- BIẾN 'app' CHO GUNICORN

@app.route('/')
def home():
    return "Bot is running! ✅"

@app.route('/health')
def health():
    return "OK", 200

# --- BOT TELEGRAM ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    button = KeyboardButton(
        text="🚀 Mở TaskHub",
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    reply_markup = ReplyKeyboardMarkup.from_button(button)
    await update.message.reply_text(
        "Chào bạn! Nhấn nút bên dưới để mở TaskHub:",
        reply_markup=reply_markup,
    )

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot đang chạy...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
