from fastapi import FastAPI
from pymongo import MongoClient

from app.settings import ATLAS_URI, DB_NAME
from app.routes.agendas import agendas


app = FastAPI(
         title="API Sadraque",
         description="Projeto Peniel",
         version="0.0.1"
     )

@app.get("/health", status_code=200)
async def health_check():
    return {"status": "ok"}

@app.on_event("startup")
def startup_db_client():
    try:
        app.mongodb_client = MongoClient(f"{ATLAS_URI}")
        app.database = app.mongodb_client[f"{DB_NAME}"]
        print("Connected to the MongoDB database!")
    except Exception:
        print("Unable to connect to the server.")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(agendas)