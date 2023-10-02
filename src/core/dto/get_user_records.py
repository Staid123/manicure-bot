from dataclasses import dataclass


@dataclass(frozen=True)
class GetUserRecordsDTO:
    phone_number: str