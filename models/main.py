import sys
from pathlib import Path
from fastapi import FastAPI
from model import Model

parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

from Scripts.Main import data_analysis

app = FastAPI()

model = Model.load_model("file_name")

@app.get("/predict_completed")
def predict():

    model.pre

@app.get("/test")
def test():
    print("hello!")
    return "hello"
<<<<<<< HEAD

@app.get("/data_analytics")
def get_analytics_result1():
    result = data_analysis()  # Call the function from data_analytics.py
    print(result)
    return result
=======
>>>>>>> a56e0b8ea930dc63612f287e5896e3087dfd38f1
