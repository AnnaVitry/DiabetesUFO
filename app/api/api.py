from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
# from  sklearn.ensemble import RandomForestClassifier

class PatientData(BaseModel):
    age: int
    gender: int
    polyuria: int
    polydipsia: int
    sudden_weight_loss: int
    weakness: int
    polyphagia: int
    visual_blurring: int
    itching: int
    irritability: int
    delayed_healing: int
    partial_paresis: int
    muscle_stiffness: int
    alopecia: int
    obesity: int

diabeast = joblib.load('model/diabeast.pkl')
app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello from root'}


@app.post('/predict')
def predict(data:PatientData):
    # Convertir les données en tableau numpy
    input_data = np.array([[value for value in data.dict().values()]])
    
    # Faire la prédiction
    prediction = diabeast.predict(input_data)[0]
    proba = diabeast.predict_proba(input_data).tolist()[0]  # Pour retourner aussi les probabilités
    
    # Retourner le résultat en JSON
    return {
        "prediction": int(prediction),
        "probabilities": {
            "negative": proba[0],
            "positive": proba[1]
        }
    }