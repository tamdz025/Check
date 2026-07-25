import logging
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# --- CẤU HÌNH ---
BOT_TOKEN = "8893681330:AAHSsMArvUSvwTXxbjDBxEzhKNW74Zb-_FE" # Thay YOUR_BOT_TOKEN bằng token bạn nhận được từ BotFather
WEB_APP_URL = "https://xacthuckey.x10.mx/0.html" # URL website của bạn

# Bật log để dễ theo dõi
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- HÀM XỬ LÝ LỆNH /start ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Gửi tin nhắn với nút bấm mở Web App."""
    # Tạo nút bấm với thuộc tính web_app
    button = KeyboardButton(
        text="🚀 Mở TaskHub",
        web_app=WebAppInfo(url=WEB_APP_URL) # Gán URL Mini App của bạn vào đây
    )
    # Tạo bàn phím và gắn nút bấm vào
    reply_markup = ReplyKeyboardMarkup.from_button(button)

    # Gửi tin nhắn kèm nút bấm
    await update.message.reply_text(
        "Chào bạn! Nhấn nút bên dưới để mở TaskHub:",
        reply_markup=reply_markup,
    )

# --- HÀM CHÍNH CHẠY BOT ---
def main() -> None:
    """Khởi chạy bot."""
    # Tạo ứng dụng và truyền Token của bot vào
    application = Application.builder().token(BOT_TOKEN).build()

    # Đăng ký handler cho lệnh /start
    application.add_handler(CommandHandler("start", start))

    # Bắt đầu chạy bot (polling)
    print("Bot đang chạy...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
