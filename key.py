import requests
import random
import string
import json

# Tạo key ngẫu nhiên với 10 số và hậu tố -NekitAOV
random_digits = ''.join(random.choices(string.digits, k=10))
key = f"{random_digits}-NekitAOV"

# URL đích với key ngẫu nhiên
destination_url = f"kiemtiennekit.x10.mx/index.html?key={key}"
long_url = destination_url

# API token và URL
api_token = '651fb4c5caa16041376bd31a'
api_url = f"https://link4m.co/api-shorten/v2?api={api_token}&url={long_url}"

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
    
    # In ra JSON
    print(json.dumps(output, indent=2, ensure_ascii=False))
        
except Exception as e:
    # Trả về JSON lỗi
    error_output = {
        "status": "error",
        "original_url": destination_url,
        "key": key,
        "shortened_url": None,
        "message": str(e)
    }
    print(json.dumps(error_output, indent=2, ensure_ascii=False))
