from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
import numpy as np
import joblib
import numpy as np
from pydantic import BaseModel
from pathlib import Path

class PatientData(BaseModel):
    age: int
    gender: int
    polyuria: int
    polydipsia: int
    sudden_weight_loss: int
    weakness: int
    polyphagia: int
    genital_thrush: int
    visual_blurring: int
    itching: int
    irritability: int
    delayed_healing: int
    partial_paresis: int
    muscle_stiffness: int
    alopecia: int
    obesity: int

# Load model with proper path handling
MODEL_PATH = Path(__file__).parent.parent.parent / 'model' / 'diabeast.pkl'

try:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    diabeast = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    raise

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello from root'}


@app.get('/health')
def health_check():
    return {'status': 'healthy'}


# --- Endpoint de prédiction ---
@app.post("/predict")
async def predict(data: PatientData):
    try:
        # Conversion des données en tableau numpy
        input_data = np.array([[value for value in data.dict().values()]])
        prediction = diabeast.predict(input_data)[0]
        proba = diabeast.predict_proba(input_data).tolist()[0]

        return {
            "prediction": int(prediction),
            "probabilities": {
                "negative": proba[0],
                "positive": proba[1]
            }
        }

    except Exception as e:
        # En cas d'erreur inattendue (ex: dimensions, type)
        raise JSONResponse(
            status_code=400,
            content={"error": "Prediction failed", "detail": str(e)}
        )
   
# curl -X POST "http://127.0.0.1:8000/predict" \
# -H "Content-Type: application/json" \
# -d '{
#   "age": 45,
#   "gender": 1,
#   "polyuria": 1,
#   "polydipsia": 0,
#   "sudden_weight_loss": 0,
#   "weakness": 1,
#   "polyphagia": 0,
#   "genital_thrush": 1,
#   "visual_blurring": 0,
#   "itching": 0,
#   "irritability": 1,
#   "delayed_healing": 0,
#   "partial_paresis": 0,
#   "muscle_stiffness": 0,
#   "alopecia": 0,
#   "obesity": 1
# }'