from fastapi import FastAPI

app = FastAPI()

@app.get("/message")
def get_message():
    return {"text": "Hello from Python 🚀"}