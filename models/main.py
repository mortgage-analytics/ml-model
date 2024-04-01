import sys
from pathlib import Path
from fastapi import FastAPI

parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

from Scripts.Main import data_analysis

app = FastAPI()

@app.get("/test")
def test():
    print("hello!")
    return "hello"

@app.get("/data_analytics")
def get_analytics_result1():
    result = data_analysis()  # Call the function from data_analytics.py
    print(result)
    return result