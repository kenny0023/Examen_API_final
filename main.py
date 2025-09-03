from fastapi import FastAPI

app = FastAPI()

# Route GET /health
@app.get("/health")
def health():
    return "OK"
