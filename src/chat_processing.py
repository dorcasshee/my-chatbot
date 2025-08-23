from typing import Any

def validate(user_msg: str) -> list[Any]:
    errors = []

    if user_msg.strip() == "": # strip whitespace
        errors.append('Please enter a message.')

    return errors