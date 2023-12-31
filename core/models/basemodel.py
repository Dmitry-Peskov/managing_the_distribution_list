from sqlalchemy import Integer
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class BaseModel(DeclarativeBase, AsyncAttrs):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.title()}Base"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement="auto",
        index=True,
        unique=True
    )
