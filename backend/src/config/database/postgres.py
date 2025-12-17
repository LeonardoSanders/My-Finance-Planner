from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from .environments import POSTGRESDB_URL

engine = create_async_engine(POSTGRESDB_URL)


async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session
