# API AI PHÂN TÍCH CẢM XÚC BẰNG VĂN BẢN

## Thông tin sinh viên
* Họ và tên: Trần Huỳnh Gia Bảo
* MSSV: 24120267

## Thông tin mô hình
* **Tên mô hình:** `lxyuan/distilbert-base-multilingual-cased-sentiments-student`
* **Liên kết Hugging Face:** [https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student](https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student)
* **Chức năng:** Phân tích cảm xúc của văn bản, hỗ trợ đa ngôn ngữ bao gồm Tiếng Việt.

## Hướng dẫn cài đặt
1. Clone repository này về máy.
2. Mở terminal tại thư mục dự án và chạy lệnh cài đặt thư viện:
    ```bash
    pip install -r requirements.txt
    ```

## Hướng dẫn chạy chương trình
```bash
uvicorn main:app --reload
```

## Hướng dẫn gọi API và ví dụ request/response
```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Đồ ăn ngon, quán đẹp!"
}'
```

## Link video
https://drive.google.com/file/d/1cFJgdELEE0x4AXcPwDN3-85JkOrV6L_m/view?usp=sharing