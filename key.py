from flask import Flask, jsonify
import requests
import random
import string

app = Flask(__name__)

def generate_key():
    # Tạo key ngẫu nhiên với 10 số và hậu tố -NekitAOV
    random_digits = ''.join(random.choices(string.digits, k=10))
    return f"{random_digits}-NekitAOV"
def generate_key1():
    # Tạo key ngẫu nhiên với 10 số và hậu tố -NekitAOV
    random_digits = ''.join(random.choices(string.digits, k=10))
    return f"{random_digits}-NekitAOV"
@app.route('/')
def shorten_all():
    key = generate_key()
    key1= generate_key1()
    destination_url = f"kiemtiennekit.x10.mx/index.html?key={key}"
    destination_url1 = f"kiemtiennekit.x10.mx/index.html?key={key1}"
    
    # API thứ nhất - Link4m
    api_token_1 = '651fb4c5caa16041376bd31a'
    api_url_1 = f"https://link4m.co/api-shorten/v2?api={api_token_1}&url={destination_url}"
    
    # API thứ hai - Bbmkts
    api_token_2 = '5c887cbed449b6c07992e454'
    api_url_2 = f"https://bbmkts.com/dapi?token={api_token_2}&longurl={destination_url1}"
    
    # Khởi tạo kết quả
    results = []
    
    try:
        # Gửi request tới Link4m
        try:
            response_1 = requests.get(api_url_1)
            result_1 = response_1.json()
            
            link4m_result = {
                "status": result_1.get("status"),
                "service": "link4m",
                "original_url": destination_url,
                "key": key,
                "shortened_url": result_1.get("shortenedUrl") if result_1.get("status") == 'success' else None,
                "message": result_1.get("message", "Unknown error") if result_1.get("status") != 'success' else "Success"
            }
            results.append(link4m_result)
        except Exception as e:
            results.append({
                "status": "error",
                "service": "link4m",
                "original_url": destination_url,
                "key": key,
                "shortened_url": None,
                "message": str(e)
            })
        
        # Gửi request tới Bbmkts
        try:
            response_2 = requests.get(api_url_2)
            result_2 = response_2.json()
            
            bbmkts_result = {
                "status": "success" if result_2.get("status") == "success" else "error",
                "service": "bbmkts",
                "original_url": destination_url1,
                "key": key1,
                "bbmktsUrl": result_2.get("bbmktsUrl") if result_2.get("status") == "success" else None,
                "message": result_2.get("msg", "Unknown error") if result_2.get("status") != "success" else "Success"
            }
            results.append(bbmkts_result)
        except Exception as e:
            results.append({
                "status": "error",
                "service": "bbmkts",
                "original_url": destination_url1,
                "key": key1,
                "bbmktsUrl": None,
                "message": str(e)
            })
        
        # Trả về danh sách kết quả
        return jsonify(results)
        
    except Exception as e:
        # Trả về JSON lỗi tổng thể
        error_output = [{
            "status": "error",
            "service": "link4m",
            "original_url": destination_url,
            "key": key,
            "shortened_url": None,
            "message": "Service unavailable"
        }, {
            "status": "error",
            "service": "bbmkts",
            "original_url": destination_url1,
            "key": key1,
            "bbmktsUrl": None,
            "message": "Service unavailable"
        }]
        return jsonify(error_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
