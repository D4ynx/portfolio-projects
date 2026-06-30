from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from db.database import Base

class StreakHistory(Base):
    __tablename__ = "streak_history"
    
    streak_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    streak_count = Column(Integer)
    streak_date = Column(Date)
    status = Column(Enum("active", "broken", "retained", name="status_enum", default="active"))
    streak_restore = Column(Integer, default = 5)
    # I think this is unnecessary.. I'll add restore instead streak_broken_reason = Column(String)