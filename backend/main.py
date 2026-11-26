import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

    print("\n=== RECEIVED ARCHITECTURE ===")
    print(
        json.dumps(
            data,
            indent=4
        )
    )

    return {
        "status": "received",
        "layer_count": len(data["layers"])
    }