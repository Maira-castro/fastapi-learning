from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import Optional

CONNECTION_STRING = f"sqlite+aiosqlite:///schema.db"

engine = create_async_engine(
    CONNECTION_STRING,
    echo=False, #pra nao printar as buscas
    pool_size = 2,
    max_overflow = 0,
    pool_timeout=30
)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class DBConnectionHandler:
    def __init__(self) -> None:
        self.session: Optional[AsyncSession]=None
    
    #*cria a sessão
    async def __aenter__(self):
        self.session = async_session()
        return self
    
    #*encerra a sessão
    async def __aexit__(self,exc_type, exc_val, exc_tb): 
        await self.session.close()