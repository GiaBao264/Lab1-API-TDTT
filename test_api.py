import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    response = requests.get(f"{BASE_URL}/")
    print("GET / ->", response.json())

def test_health():
    response = requests.get(f"{BASE_URL}/health")
    print("GET /health ->", response.json())

def test_predict_success():
    headers = {"Content-Type": "application/json"}

    data_positive = {"text": "Món ăn ngon quá."}
    res_pos = requests.post(f"{BASE_URL}/predict", headers=headers, json=data_positive)
    print("\nPOST /predict (Tích cực) ->")
    print(json.dumps(res_pos.json(), indent=2, ensure_ascii=False))

    data_negative = {"text": "Phục vụ chậm chạp, đồ ăn khá dở."}
    res_neg = requests.post(f"{BASE_URL}/predict", headers=headers, json=data_negative)
    print("\nPOST /predict (Tiêu cực) ->")
    print(json.dumps(res_neg.json(), indent=2, ensure_ascii=False))

def test_predict_error():
    headers = {"Content-Type": "application/json"}
    data_empty = {"text": "   "}
    res_err = requests.post(f"{BASE_URL}/predict", headers=headers, json=data_empty)
    print("\nPOST /predict (Lỗi input) ->", res_err.status_code, res_err.json())

if __name__ == "__main__":
    print("--- TESTING API ---")
    test_root()
    test_health()
    test_predict_success()
    test_predict_error()