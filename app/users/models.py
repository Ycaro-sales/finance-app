from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"

    id: Mapped[int]
    email: Mapped[str]
    password: Mapped[str]
