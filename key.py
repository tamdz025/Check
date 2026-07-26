from flask import Flask, jsonify
import requests
import random
import string

app = Flask(__name__)

@app.route('/')
def shorten():
    # Tạo key ngẫu nhiên với 10 số và hậu tố -NekitAOV
    random_digits = ''.join(random.choices(string.digits, k=10))
    key = f"{random_digits}-NekitAOV"
    
    # URL đích với key ngẫu nhiên
    destination_url = f"kiemtiennekit.x10.mx/index.html?key={key}"
    
    # API token và URL
    api_token = '651fb4c5caa16041376bd31a'
    api_url = f"https://link4m.co/api-shorten/v2?api={api_token}&url={destination_url}"
    
    try:
        # Gửi request tới API
        response = requests.get(api_url)
        result = response.json()
        
        # Tạo response JSON
        output = {
            "status": result.get("status"),
            "original_url": destination_url,
            "key": key,
            "shortened_url": result.get("shortenedUrl") if result.get("status") == 'success' else None,
            "message": result.get("message", "Unknown error") if result.get("status") != 'success' else "Success"
        }
        
        return jsonify(output)
        
    except Exception as e:
        # Trả về JSON lỗi
        error_output = {
            "status": "error",
            "original_url": destination_url,
            "key": key,
            "shortened_url": None,
            "message": str(e)
        }
        return jsonify(error_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
