from src.core.dao import AbstractDAO
from src.core.dto import GetAllRecordsDTO, DeleteRecordDTO, InsertrecordDTO

from abc import abstractmethod


class AdminAbstractDAO(AbstractDAO):
    @abstractmethod
    async def insert_record(self, dto: InsertrecordDTO) -> None:
        pass
    @abstractmethod
    async def get_all_records(self, dto: GetAllRecordsDTO) -> None:
        pass
    @abstractmethod
    async def delete_record(self, dto: DeleteRecordDTO) -> None:
        pass