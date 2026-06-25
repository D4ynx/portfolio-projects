from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from datetime import datetime
from db.database import Base

class Guild(Base):
    __tablename__ = "guild"
    
    guild_id = Column(Integer, primary_key=True, index=True)
    guild_name = Column(String, unique=True)
    guild_description = Column(String)
    status = Column(Enum("active", "inactive", name = "guild_status_enum"), default="active")
    created_by = Column(Integer, ForeignKey("users.user_id"))
    created_at = Column(DateTime, default=datetime.utcnow)
