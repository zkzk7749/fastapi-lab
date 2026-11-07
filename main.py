import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI!",
        "instance": os.getenv("INSTANCE_NAME", "local")
    }


@app.get("/health")
def health():
    return {"status": "ok"}