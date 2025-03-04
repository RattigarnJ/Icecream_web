from fastapi import FastAPI
from pydantic import BaseModel
import torch  # ถ้าใช้โมเดล PyTorch
import tensorflow as tf  # ถ้าใช้โมเดล TensorFlow

app = FastAPI()

class InputData(BaseModel):
    text: str

# โหลดโมเดล (เลือกใช้ 1 วิธีตามประเภทโมเดล)
MODEL_PATH = "model.pth"  # หรือ "model.pkl" / "model.h5"
model = None  # ตัวแปรโมเดล (เป็น global variable)

@app.on_event("startup")
def load_model():
    global model
    try:
        model = torch.load(MODEL_PATH, map_location=torch.device("cpu"))  # PyTorch
        model.eval()  # ตั้งเป็น evaluation mode
        print("✅ Model loaded successfully!")
    except Exception as e:
        print(f"❌ Error loading model: {e}")

@app.get("/")
def read_root():
    return {"message": "API is running!"}

@app.post("/predict")
def predict(data: InputData):
    response = f"AI ตอบ: {data.text}"
    return {"response": response}
