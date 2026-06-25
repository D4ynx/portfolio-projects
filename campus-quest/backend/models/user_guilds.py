from sqlalchemy import Column, Integer, String, Date, UniqueConstraint, ForeignKey, Enum
from db.database import Base
from datetime import datetime


# Junction Table User <-> Guilds
class UserGuild(Base):
    __tablename__ = "user_guild"
    
    user_guild_id = Column(Integer, primary_key=True, index=True)
    guild_id = Column(Integer, ForeignKey("guild.guild_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    joined_at = Column(Date, default = datetime.utcnow)
    role = Column(Enum("guild_master", "officer", "member", name = "role_status_enum"))
    rank = Column(Enum("gold", "silver", "bronze", name = "rank_enum"), default = "bronze")
    xp_contributed = Column(Integer)
    last_activity = Column(Date)
    
    __table_args__ = (UniqueConstraint("guild_id", "user_id"),)