from asyncpg import Connection


async def _create_admin_table(connect: Connection) -> None:
    await connect.execute(
        '''
        CREATE TABLE IF NOT EXISTS records(
            PRIMARY KEY(id),
            id SERIAL NOT NULL,
            client_name text,
            phone_number text,
            type_of_service text,
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
            phone_number text,
            type_of_service text,
            datetime timestamp
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