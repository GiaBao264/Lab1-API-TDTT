from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(
    title="Sentiment Analysis API",
    description="API phân tích cảm xúc văn bản sử dụng Hugging Face",
    version="1.0.0"
)

try:
    classifier = pipeline(
        "sentiment-analysis", 
        model="lxyuan/distilbert-base-multilingual-cased-sentiments-student"
    )
except Exception as e:
    classifier = None
    print(f"Lỗi khi tải mô hình: {e}")

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    """Thông tin giới thiệu."""
    return {
        "message": "Welcome to Sentiment Analysis API",
        "model": "lxyuan/distilbert-base-multilingual-cased-sentiments-student",
        "usage": "Gửi POST request chứa {'text': 'nội dung'} tới /predict"
    }

@app.get("/health")
def health_check():
    """Kiểm tra trạng thái hoạt động."""
    if classifier is None:
        raise HTTPException(status_code=500, detail="Mô hình chưa được tải thành công")
    return {"status": "healthy", "model_loaded": True}

@app.post("/predict")
def predict_sentiment(request: TextRequest):
    """Nhận dữ liệu đầu vào, gọi mô hình và trả về kết quả."""
    if not request.text or request.text.strip() == "":
        raise HTTPException(status_code=400, detail="Văn bản đầu vào không được để trống")
    
    if classifier is None:
        raise HTTPException(status_code=500, detail="Hệ thống đang lỗi, không thể suy luận")

    try:
        result = classifier(request.text)
        return {
            "input": request.text, 
            "prediction": result[0]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi trong quá trình suy luận: {str(e)}")