from fastapi import FastAPI
import joblib
# from  sklearn.ensemble import RandomForestClassifier

diabeast = joblib.load('model/diabeast.pkl')
diabeast.predict()
app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello from root'}


@app.post('/predict')
def predict(**args):
    resultat = ''
    return {'result': resultat}