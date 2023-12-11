from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from .base import BaseModel


class User(BaseModel):
    fullname: Mapped[str] = mapped_column(
        String(100),
        index=True,
        nullable=False
    )
    group: Mapped[str] = mapped_column(
        String(100),
        index=True,
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(100),
        index=True,
        nullable=False
    )
    isCurrentEmployee: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )
    isEnabled: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )
