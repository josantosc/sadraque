import re
def validate_name(value: dict) -> bool:
    result_value = {k: v for k, v in value.items() if v is not None}
    if len(result_value) >= 1:
        return True
    else:
        False
def validate_type_agenda(value: dict) -> bool:
    result_value = {k: v for k, v in value.items() if v is not None}
    if len(result_value) == 1 and type(result_value) == int:
        return True
    else:
        False
