from asyncpg import Connection
from src.core.dto import InsertrecordDTO, GetAllRecordsDTO, DeleteRecordDTO
from src.core.dao import AdminAbstractDAO

from typing import Optional, List


class AdminDAO(AdminAbstractDAO):
    __slots__ = ('connect', )

    def __init__(self, connect: Connection) -> None:
        self.connect = connect    


    async def insert_record(self, dto: InsertrecordDTO) -> None:
        connect = self.connect
        async with connect.transaction():
            await connect.execute(
                '''
                INSERT INTO records(client_name, phone_number, datetime, type_of_service) VALUES($1, $2, $3, $4)
                ''', dto.client_name, dto.phone_number, dto.datetime, dto.type_of_service
            )


    async def get_all_records(self) -> Optional[List]:
        connect = self.connect
        async with connect.transaction():
            data = await connect.fetch(
                '''
                SELECT client_name, phone_number, datetime, type_of_service
                FROM records
                '''
            )
        return [GetAllRecordsDTO(**rec) for rec in data]
    

    async def delete_record(self, dto: DeleteRecordDTO) -> None:
        connect = self.connect
        async with connect.transaction():
            await connect.execute(
                '''
                DELETE FROM records WHERE datetime = $1
                ''', dto.datetime
            )