from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def test():
    print("hello!")
    return "hello"