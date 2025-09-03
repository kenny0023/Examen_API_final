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

# Route GET /phones
@app.get("/phones", response_model=List[Phone])
def get_phones():
    return phones_db

# Route GET /phones/{id}
from fastapi import HTTPException

@app.get("/phones/{id}", response_model=Phone)
def get_phone(id: str):
    for phone in phones_db:
        if phone.identifier == id:
            return phone
    raise HTTPException(status_code=404, detail=f"Le phone avec l'id '{id}' n'existe pas ou n'a pas été trouvé.")

# BONUS : PUT /phones/{id}/characteristics
@app.put("/phones/{id}/characteristics", response_model=Phone)
def update_characteristics(id: str, characteristics: Characteristic):
    for phone in phones_db:
        if phone.identifier == id:
            phone.characteristics = characteristics
            return phone
    raise HTTPException(status_code=404, detail=f"Le phone avec l'id '{id}' n'existe pas ou n'a pas été trouvé.")
