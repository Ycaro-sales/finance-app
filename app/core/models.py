from sqlalchemy import ForeignKey
from app.db.base import Base
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(str, nullable=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)


class Balance(Base):
    __tablename__ = "balance"

    owner_id: Mapped[int] = mapped_column(int, nullable=False)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    amount: Mapped[float] = mapped_column(float, nullable=False)


class Movement(Base):
    __tablename__ = "movements"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    amount: Mapped[float] = mapped_column(float, nullable=False)
    description: Mapped[str]

    parent_transaction_id: Mapped[int] = mapped_column(
        ForeignKey("movements.id"), nullable=True
    )

    scheduled_at: Mapped[datetime] = mapped_column(datetime, nullable=False)
    executed_at: Mapped[datetime]


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(str, nullable=False)


class GroupMembers(Base):
    __tablename__ = "group_members"

    group_id: Mapped[int] = mapped_column(int, nullable=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(int, nullable=False, primary_key=True)


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(str, nullable=False)


class MovementTag(Base):
    __tablename__ = "movement_tags"

    movement_id: Mapped[int] = mapped_column(int, nullable=False, primary_key=True)
    tag_id: Mapped[int] = mapped_column(int, nullable=False, primary_key=True)


class MovementTags(Base):
    __tablename__ = "movement_tags"

    movement_id: Mapped[int] = mapped_column(int, nullable=False, primary_key=True)
    tag_id: Mapped[int] = mapped_column(int, nullable=False, primary_key=True)


class Recurrence(Base):
    __tablename__ = "recurrences"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    movement_id: Mapped[int] = mapped_column(int, nullable=False)
    frequency: Mapped[str] = mapped_column(str, nullable=False)


class UserAccounts(Base):
    __tablename__ = "user_accounts"

    user_id: Mapped[int] = mapped_column(int, nullable=False, primary_key=True)
    account_id: Mapped[int] = mapped_column(int, nullable=False, primary_key=True)
