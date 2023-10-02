from asyncpg import Connection
from src.core.dto.get_all_users import GetAllRecordsDTO
from src.core.dao import UserAbstractDAO
from src.core.dto import GetUserRecordsDTO, InsertrecordDTO

from datetime import datetime


class UserDAO(UserAbstractDAO):
    __slots__ = ('connect', )

    def __init__(self, connect: Connection) -> None:
        self.connect = connect


    async def get_rec_by_phone(self, dto: GetUserRecordsDTO) -> list[GetAllRecordsDTO]:
        connect = self.connect
        async with connect.transaction():
            data = await connect.fetch(
                '''
                SELECT phone_number, datetime, type_of_service FROM records
                WHERE phone_number = $1
                ''', dto.phone_number
            )
        return [GetAllRecordsDTO(**rec) for rec in data]
    

    async def insert_record(self, dto: InsertrecordDTO) -> None:
        connect = self.connect
        async with connect.transaction():
            await connect.execute(
                '''
                INSERT INTO clients(client_id, phone_number, datetime, type_of_service) 
                VALUES($1, $2, $3, $4)
                ''', dto.client_id, dto.phone_number, dto.datetime, dto.type_of_service
            )
    
    async def get_all_records(self) -> list[GetAllRecordsDTO]:
        connect = self.connect
        data = await connect.fetch(
            '''
            SELECT client_id, phone_number, datetime, type_of_service FROM clients
            '''
        )
        return [GetAllRecordsDTO(**rec) for rec in data]
    

    async def check_record(self, datetime: datetime) -> bool:
        connect = self.connect
        data = await connect.fetch(
            '''
            SELECT COUNT(*) FROM clients
            WHERE datetime = $1
            ''', datetime
        )
        return data[0][0]