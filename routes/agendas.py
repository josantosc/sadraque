import logging
from fastapi import APIRouter,  Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from bson.objectid import ObjectId
from pydantic import ValidationError
# from schema.agenda import agendaEntity, agendasEntity
from model.agendas import Agenda, AgendaUpdate

logging = logging.Logger("zapi_client")
agendas = APIRouter()


@agendas.get('/agendas', response_description="List all agendas", response_model=List[Agenda])
async def find_all_agendas(request: Request):
    try:
        agendas = list(request.app.database["agendas"].find(limit=100))
        return agendas

    except ValidationError as e:
        logging.error("Error in validate agendas: %s", e)
        raise e


@agendas.get('/agendas/{id}', response_description="Get a single agenda by id", response_model=Agenda)
async def find_agenda(id: str, request: Request):
    if (agenda := request.app.database["agendas"].find_one({"_id": id})) is not None:
        return agenda
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Agenda with ID {id} not found")



@agendas.post('/agendas', response_description="Create a new agenda", status_code=status.HTTP_201_CREATED, response_model=Agenda)
async def create_agenda(request: Request, agenda: Agenda = Body(...)):
    try:
        agenda = jsonable_encoder(agenda)
        new_agenda = request.app.database["agendas"].insert_one(agenda)
        created_agenda = request.app.database["agendas"].find_one(
                {"_id": new_agenda.inserted_id}
        )
        return created_agenda

    except ValidationError as e:
        logging.error("Error in validate create agendas: %s", e)
        raise e



@agendas.put("/{id}", response_description="Update a agenda", response_model=Agenda)
async def update_agenda(id: str, request: Request, agenda: AgendaUpdate = Body(...)):
    agenda = {k: v for k, v in agenda.dict().items() if v is not None}

    if len(agenda) >= 1:
        update_result = request.app.database["agendas"].update_one(
            {"_id": ObjectId(id)}, {"$set": agenda}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Agenda with ID {id} not found")

    if (
        existing_agenda := request.app.database["agendas"].find_one({"_id": ObjectId(id)})
    ) is not None:
        return existing_agenda

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Agenda with ID {id} not found")



@agendas.delete("/{id}", response_description="Delete a agenda")
async def delete_agenda(id: str, request: Request, response: Response):
    delete_result = request.app.database["agendas"].delete_one({"_id": ObjectId(id)})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Agenda with ID {id} not found")