def agendaEntity(item) -> dict:
    return {
        "type_agenda": item["_id"],
        "name": item["name"],
        "created_at": item["created_at"]
    }


def agendasEntity(entity) -> list:
    return [agendaEntity(item) for item in entity]
