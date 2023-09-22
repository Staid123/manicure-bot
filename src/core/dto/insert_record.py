from dataclasses import dataclass 


@dataclass(frozen=True)
class InsertrecordDTO:
    client_name: str
    phone_number: str
    type_of_service: str
    datetime: str
