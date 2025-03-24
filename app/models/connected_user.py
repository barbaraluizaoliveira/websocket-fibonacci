from sqlalchemy import Column, Integer, String, DateTime
from app.db import Base
from datetime import datetime, timezone

class ConnectedUser(Base):
    __tablename__ = "connected_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True, nullable=False)
    connected_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
