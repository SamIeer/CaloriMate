from fastapi import FastAPI
import pandas as pd
from app.schema import ModelInput
import joblib 

app = FastAPI()   # initialise a fastapi app 

model = joblib.load("Model/calorie_model.pkl")

@app.get("/")     # creating a path operations (GET, POST)
async def root(): # A async functions defines the path operation
    return {"message": "Wellcome to  CaloriMate API - Predict your calori "} # returning the content

@app.get("/health") # EndPoint for health
def health_check(): 
    return {"status": "healthy"}

@app.post("/pedict") #Endpoint for predict 
def predict_calori(data: ModelInput):
    # Convert request into dataframe
    input_data = pd.DataFrame([data.model_dump()])
    # Predict
    prediction = model.predict(input_data)[0]
    return {"Your calori Burn": round(float(prediction),2)}

# This is a working app 
# Don't slack off bro 
# Last ONE 