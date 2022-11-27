from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, validator
from bson.objectid import ObjectId

# class GetObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate
#
#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid objectid")
#         return ObjectId(v)
#
#     @classmethod
#     def __modify_schema__(cls, field_schema):
#         field_schema.update(type="string")

class Agenda(BaseModel):
    title: str = Field(...)
    date: list[int] = Field(...)
    description: Optional[str] = Field(...)
    time: Optional[str] = Field(...)
    created_at: Optional[datetime] = datetime.now()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
             "title": "Culto de Jovens",
             "date": ['01'],
             "description": "Descrição maneira!",
             "time": "HH:mm"

            }
        }

class AgendaUpdate(BaseModel):
    title: str = Field(...)
    name: list = Field(...)

    class Config:
        schema_extra = {
            "example": {
             "title": "Culto de Jovens",
             "data": ['01']
            }
        }
        