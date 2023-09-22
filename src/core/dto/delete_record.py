from dataclasses import dataclass


@dataclass(frozen=True)
class DeleteRecordDTO:
    datetime: str