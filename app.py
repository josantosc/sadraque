
# from fastapi import FastAPI
# from routes.agendas import agendas

# app = FastAPI(
#         title="API Projeto Peniel",
#         description="Sadraque",
#         version="0.0.1"
#     )


# app.include_router(agendas)

# @app.get("/", status_code=200)
# async def health_check():
#     return {"status": "ok"}

from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes.agendas import agendas

config = dotenv_values(".env")

app = FastAPI(
         title="API Sadraque",
         description="Projeto Peniel",
         version="0.0.1"
     )

@app.get("/", status_code=200)
async def health_check():
    return {"status": "ok"}

@app.on_event("startup")
def startup_db_client():
    
    try:
        app.mongodb_client = MongoClient(config["ATLAS_URI"])
        app.database = app.mongodb_client[config["DB_NAME"]]
        print("Connected to the MongoDB database!")
    except Exception:
        print("Unable to connect to the server.")   

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(agendas)