from dataclasses import dataclass


@dataclass(frozen=True)
class GetAllRecordsDTO:
    client_name: str
    phone_number: str
    datetime: str
    type_of_service: str