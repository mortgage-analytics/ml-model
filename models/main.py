import sys
import numpy as np
from pathlib import Path
from fastapi import FastAPI
from xgboost_model import Model as XGBoostModel
from pydantic import BaseModel

parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

from Scripts.Main import data_analysis

app = FastAPI()

model = XGBoostModel(5)
model.load("xgboost_model_weights")

class ModelData(BaseModel):
    application_type: int
    mortgage_type: int
    property_value: float
    mortgage_amount_proposed: float
    summed_income: float

    def to_np(self):
        return np.array([self.application_type,
                         self.mortgage_type,
                         self.property_value,
                         self.mortgage_amount_proposed,
                         self.summed_income])

@app.get("/")
def home():
    return

@app.get("/data_analytics")
def get_analytics_result1():
    result = data_analysis()  # Call the function from data_analytics.py
    print(result)
    return result

@app.post("/model")
def predict_successful_mortgage(data:ModelData):
    return model.infer(data.to_np())
