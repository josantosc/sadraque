from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator
from bson.objectid import ObjectId

class GetObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class Agenda(BaseModel):
    type_agenda: dict = Field(...)
    name: dict = Field(...)
    created_at: Optional[datetime] = datetime.now()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "type_agenda": {"_id": 1},
                "name":
                            {
                            "description" : "Culto de Jovens",
                            "data" : "Todos os Sábados"
                            }
                }
        }


class AgendaUpdate(BaseModel):
    type_agenda: Optional[dict]
    name: Optional[dict]

    class Config:
        schema_extra = {
                "type_agenda": {"_id": 1},
                "name" :
                            {
                            "description" : "Culto de Jovens",
                            "data" : "Todos os Sábados"
                            }
                    
            }
        