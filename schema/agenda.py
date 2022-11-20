def agendaEntity(item) -> dict:
    return {
        "id": item["id"],
        "descricao": item["descricao"],
        "data": item["data"]
    }


def agendasEntity(entity) -> list:
    return [agendaEntity(item) for item in entity]
