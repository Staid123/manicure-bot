from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class GetAllRecordsDTO:
    phone_number: str
    datetime: datetime
    type_of_service: str
    client_name: str | None = None
    client_id: str | None = None