from app.db.engine import engine
from sqlalchemy.ext.asyncio import AsyncSession


async def get_db():
    async with AsyncSession(engine) as session:
        yield session
