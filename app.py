from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

class Input (BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float
    

model = joblib.load ("mymodel.pkl")


@app.post("/predict/")
async def predict_fraud (input: Input):
    input_data = pd.DataFrame ([input.model_dump()])

    prediction = model.predict (input_data)

    proba = model.predict_proba (input_data)

    return {

        'prediction': int (prediction[0])
        
    }