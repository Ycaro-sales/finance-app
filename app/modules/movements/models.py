from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Movement(Base):
    __tablename__ = "movements"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    value: Mapped[float] = mapped_column(float, nullable=False)
    description: Mapped[str]
