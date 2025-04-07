from datetime import datetime

from sqlalchemy import Integer, String, func
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.core.database import Base


class TronLogging(Base):
    __tablename__ = "tron"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, auto_increment=True)
    address: Mapped[str] = mapped_column(String, nullable=False)
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())
