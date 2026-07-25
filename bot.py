from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

BOT_TOKEN = '8893681330:AAHSsMArvUSvwTXxbjDBxEzhKNW74Zb-_FE'
DOMAIN = 'https://xacthuckey.x10.mx/0.html'

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        update = request.get_json()
        
        if 'message' in update:
            chat_id = update['message']['chat']['id']
            text = update['message'].get('text', '')
            
            if text == '/start':
                message = "🤖 Chào mừng bạn đến với TaskHub!\n\n" \
                         "📌 Làm nhiệm vụ kiếm thưởng mỗi ngày\n" \
                         "💰 +100đ cho mỗi nhiệm vụ\n" \
                         "💳 Rút tiền tối thiểu 30,000đ\n\n" \
                         "🔽 Nhấn nút bên dưới để bắt đầu:"
                
                keyboard = {
                    'inline_keyboard': [
                        [
                            {
                                'text': '🚀 Mở TaskHub',
                                'web_app': {'url': DOMAIN}
                            }
                        ]
                    ]
                }
                
                send_message(chat_id, message, keyboard)
            elif text == '/help':
                send_message(chat_id, "📖 Hướng dẫn sử dụng:\n\n1️⃣ Nhấn '🚀 Mở TaskHub'\n2️⃣ Làm nhiệm vụ kiếm thưởng\n3️⃣ Xác thực key nhận tiền\n4️⃣ Rút tiền về ngân hàng/thẻ cào")
            else:
                send_message(chat_id, "🤖 Gửi /start để bắt đầu!")
        
        return jsonify({'status': 'ok'}), 200
    except Exception as e:
        print(f"Lỗi: {e}")
        return jsonify({'status': 'error'}), 500

def send_message(chat_id, text, keyboard=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': text
    }
    if keyboard:
        data['reply_markup'] = json.dumps(keyboard)
    
    try:
        response = requests.post(url, data=data)
        return response.json()
    except Exception as e:
        print(f"Lỗi gửi tin nhắn: {e}")
        return None

@app.route('/', methods=['GET'])
def index():
    return "🤖 Bot đang hoạt động!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
