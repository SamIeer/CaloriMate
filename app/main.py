from fastapi import FastAPI
import pandas as pd
from app.schema import ModelInput
import joblib 

app = FastAPI()   # initialise a fastapi app 

model = joblib.load("../Model/calorie_model.joblib")

@app.get("/")     # creating a path operations (GET, POST)
async def root(): # A async functions defines the path operation
    return {"message": "Wellcome to  CaloriMate API - Predict your calori "} # returning the content

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/pedict")
def predict_calori(data: ModelInput):
    input_data = pd.dataframe([data.model_dump()])
    prediction = model.predict(input_data)[0]
    return {"Your calori Burn": round(float(prediction),2)}

