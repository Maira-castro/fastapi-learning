from src.models.entities.users import Users
from src.models.setting.database_connection_handler import DBConnectionHandler
from sqlalchemy import insert, select
from .interfaces.users_repository import UsersRepositoryInterface

class UsersRepository(UsersRepositoryInterface):
    async def insert_users(self, user_infor: dict) -> None:
        async with DBConnectionHandler() as db:
            query = insert(Users).values(**user_infor)
            await db.session.execute(query)
            await db.session.commit()

    async def get_users_by_name(self, user_name:str) -> list[dict]:
        async with DBConnectionHandler() as db:
            query = (
                select(Users)
                .where(Users.c.user_name == user_name)
            )
            result = await db.session.execute(query)
            rows = result.fetchall()

            users_list = [dict(row._mapping) for row in rows]
            return users_list