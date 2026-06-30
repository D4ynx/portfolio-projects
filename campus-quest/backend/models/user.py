from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from db.database import Base

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    user_email = Column(String, unique=True)
    user_password = Column(String) ##have to hash this in the future
    name = Column(String)
    user_xp = Column(Integer, default=0)
    user_streak = Column(Integer, default=0)

class Achievement(Base):
    __tablename__ = "achievement"
    
    achievement_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String, unique=True)
    achievement_xp = Column(Integer)
    condition = Column(String)


    
#Junction Table User <-> Achievement
class UserAchievement(Base):
    __tablename__ = "user_achievement"
    
    achievement_id = Column(Integer, ForeignKey("achievement.achievement_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    date_achieved = Column(Date)
    xp_gained = Column(Integer)
    
    __table_args__ = (PrimaryKeyConstraint("achievement_id", "user_id"), )
    
    

    