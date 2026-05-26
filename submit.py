import urllib.request
import json

req = urllib.request.Request('http://127.0.0.1:8080/submit', data=json.dumps({"branch": "jules-15253088997197693656-5f8d9957", "commit": "9ab2967982a3835abbf3b2a50b06679e35a41d4a"}).encode('utf-8'))
req.add_header('Content-Type', 'application/json')
try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
