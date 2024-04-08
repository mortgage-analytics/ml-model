import sys
from pathlib import Path
from fastapi import FastAPI
from model import Model

parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

from Scripts.Main import data_analysis

app = FastAPI()

model = Model.load_model("file_name")

@app.get("/data_analytics")
def get_analytics_result1():
    result = data_analysis()  # Call the function from data_analytics.py
    print(result)
    return result
