from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Route GET /health
@app.get("/health")
def health():
    return "OK"

# Modèle pour les caractéristiques
class Characteristic(BaseModel):
    ram_memory: float
    rom_memory: float
    
# Modèle pour un téléphone
class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic
    
# Stockage en mémoire
phones_db: List[Phone] = []

# Route POST /phones
@app.post("/phones", status_code=status.HTTP_201_CREATED)
def create_phones(phones: List[Phone]):
    phones_db.extend(phones)
    return {"message": "Phones added", "count": len(phones)}
