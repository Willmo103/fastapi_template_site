from sqlalchemy import Column, String, Integer, TIMESTAMP, text, ForeignKey
from app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)

    password = Column(String, nullable=False)

    email = Column(String, nullable=False)

    username = Column(String, nullable=False)

    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
