from abc import abstractmethod
from src.core.dao import AbstractDAO
from src.core.dto import GetUserRecordsDTO, InsertrecordDTO, GetAllRecordsDTO


class UserAbstractDAO(AbstractDAO):
    @abstractmethod
    async def get_rec_by_phone(self, dto: GetUserRecordsDTO) -> None:
        pass

    @abstractmethod
    async def insert_record(self, dto: InsertrecordDTO) -> None:
        pass

    @abstractmethod
    async def get_all_records(self, dto: GetAllRecordsDTO) -> None:
        pass