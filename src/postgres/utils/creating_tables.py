from asyncpg import Connection


async def _create_admin_table(connect: Connection) -> None:
    await connect.execute(
        '''
        CREATE TABLE IF NOT EXISTS records(
            PRIMARY KEY(id),
            id SERIAL NOT NULL,
            client_name TEXT,
            phone_number char(12),
            type_of_service TEXT,
            datetime timestamp
        );
        '''
    )


async def _create_user_table(connect: Connection) -> None:
    await connect.execute(
        '''
        CREATE TABLE IF NOT EXISTS clients(
            PRIMARY KEY(id),
            id SERIAL NOT NULL,
            type_of_service TEXT,
            datetime timestamp,
            phone_number BIGINT
        );
        '''
    )


async def _drop_tables(connect: Connection) -> None:
    await connect.execute(
        '''
        DROP TABLE IF EXISTS records, clients
        '''
    )


async def creating_tables(connect: Connection, force: bool = False) -> None:
    if force:
        await _drop_tables(connect)
    await _create_admin_table(connect)
    await _create_user_table(connect)