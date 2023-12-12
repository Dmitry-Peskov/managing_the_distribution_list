from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result

from core.models import User
from .schemas import UserCREATE


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.isEnabled.desc(), User.fullname.asc())
    answer: Result = await session.execute(stmt)
    users = answer.scalars().all()
    return list(users)


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, new_user: UserCREATE) -> User:
    user = User(**new_user.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
