from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from db.database import Base

# for personal quests
class Quest(Base):
    __tablename__ = "quests"
    
    quest_id = Column(Integer, primary_key=True, index=True)
    quest_name = Column(String)
    quest_description = Column(String)
    xp_earned = Column(Integer)
    quest_deadline = Column(Date)
    quest_status = Column(Enum("completed", "incomplete", "not_started", name="quest_status_enum"),  default = "not_started") 
    user_id = Column(Integer, ForeignKey("users.user_id"))
    
#Junction Table Guild <-> Quest
class GuildQuest(Base):
    __tablename__ = "guild_quest"
    
    quest_id = Column(Integer, ForeignKey("quests.quest_id"))
    guild_id = Column(Integer, ForeignKey("guild.guild_id"))
    quest_name = Column(String)
    xp_earned = Column(Integer)
    date_achieved = Column(Date)
    description = Column(String)
    
    __table_args__ = (PrimaryKeyConstraint("quest_id", "guild_id"),)