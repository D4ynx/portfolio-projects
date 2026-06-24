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
    
class Guild(Base):
    __tablename__ = "guild"
    
    guild_id = Column(Integer, primary_key=True, index=True)
    guild_name = Column(String, unique=True)
    guild_description = Column(String, unique=True)

class Achievement(Base):
    __tablename__ = "achievement"
    
    achievement_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String, unique=True)
    achievement_xp = Column(Integer)
    condition = Column(String)

class StreakHistory(Base):
    __tablename__ = "streak_history"
    
    streak_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    count = Column(Integer)
    streak_date = Column(Date)
    status = Column(Enum("active", "broken", "retained", name="status_enum", default="active"))
    streak_broken_reason = Column(String) #Will convert to ENUM

# Junction Table User <-> Guilds
class UserGuild(Base):
    __tablename__ = "user_guild"
    
    user_guild_id = Column(Integer, primary_key=True, index=True)
    guild_id = Column(Integer, ForeignKey("guild.guild_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    joined_at = Column(Date)
    role = Column(String) #Will convert to ENUM [guild_master, officer, member]
    rank = Column(String) #Will convert to ENUM [bronze, silver, gold]
    status = Column(String) #Wll convert to ENUM [active, inactive]
    xp_contributed = Column(Integer)
    last_activity = Column(Date)
    
    __table_args__ = (UniqueConstraint("guild_id", "user_id", "status"),)

    
#Junction Table User <-> Achievement
class UserAchievement(Base):
    __tablename__ = "user_achievement"
    
    achievement_id = Column(Integer, ForeignKey("achievement.achievement_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    date_achieved = Column(Date)
    xp_gained = Column(Integer)
    
    __table_args__ = (PrimaryKeyConstraint("achievement_id", "user_id"), )
    
    

    