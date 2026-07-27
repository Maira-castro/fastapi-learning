from .database_connection_handler import DBConnectionHandler
import pytest

@pytest.mark.asyncio
@pytest.mark.skip(reason='connecting with DB')
async def test_connection():
    async with DBConnectionHandler() as db_handler:
        print(db_handler.session)
        assert db_handler.session is not None
