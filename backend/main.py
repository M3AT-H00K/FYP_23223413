import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model_builder import build_model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Backend is working!"
    }

@app.post("/architecture")
def receive_architecture(data: dict):

    model = build_model(data)

    print("\n=== GENERATED MODEL ===\n")

    print(model)

    return {
        "status": "received",
        "layer_count": len(data["layers"])
    }