from uuid import UUID


def is_valid_uuid4(input_uuid: str) -> bool:
    try:
        val = UUID(input_uuid, version=4)
    except ValueError:
        # If it's a value error, then the string
        # is not a valid hex code for a UUID.
        return False
    return True
