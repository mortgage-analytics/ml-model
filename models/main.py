from fastapi import FastAPI
from model import Model

app = FastAPI()

model = Model.load_model("file_name")

@app.get("/predict_completed")
def predict():

    model.pre

@app.get("/test")
def test():
    print("hello!")
    return "hello"
