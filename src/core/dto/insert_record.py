from dataclasses import dataclass 


@dataclass(frozen=True)
class InsertrecordDTO:
    phone_number: str
    type_of_service: str
    datetime: str
    client_name: str | None = None
    client_id: str | None = None
