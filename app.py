import requests
import time
import json

BOT_TOKEN = '8893681330:AAHSsMArvUSvwTXxbjDBxEzhKNW74Zb-_FE'
DOMAIN = 'https://xacthuckey.x10.mx'

def send_message(chat_id, text, keyboard=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {'chat_id': chat_id, 'text': text}
    if keyboard:
        data['reply_markup'] = json.dumps(keyboard)
    
    try:
        response = requests.post(url, data=data)
        return response.json()
    except Exception as e:
        print(f"Lỗi: {e}")
        return None

print("🤖 Bot đang chạy (Polling mode)...")
offset = 0

while True:
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
        response = requests.get(url, params={'offset': offset, 'timeout': 30})
        data = response.json()
        
        if data['ok']:
            for update in data['result']:
                if 'message' in update:
                    chat_id = update['message']['chat']['id']
                    text = update['message'].get('text', '')
                    
                    if text == '/start':
                        keyboard = {
                            'inline_keyboard': [
                                [{'text': '🚀 Mở TaskHub', 'web_app': {'url': DOMAIN}}]
                            ]
                        }
                        send_message(chat_id, "🤖 Chào mừng! Nhấn nút bên dưới:", keyboard)
                    else:
                        send_message(chat_id, "🤖 Gửi /start để bắt đầu!")
                    
                    offset = update['update_id'] + 1
        
        time.sleep(2)
    except Exception as e:
        print(f"Lỗi: {e}")
        time.sleep(5)
