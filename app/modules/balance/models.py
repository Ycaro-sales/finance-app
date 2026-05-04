from app.db.base import Base


class Movement(Base):
    __tablename__ = "movements"

    id: int
    name: str
    description: str
