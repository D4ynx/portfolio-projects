from sqlalchemy.orm import Session
from models import Guild, UserGuild
from fastapi import HTTPException 

def verify_guild(guild_id: int, db: Session):
    guild = db.query(Guild).filter(Guild.guild_id == guild_id).first()
    if not guild:
        raise HTTPException(status_code=404, detail="Guild does not exist")
    else:
        return guild
    
def verify_membership(guild_id: int, user_id: int, db: Session):
    userguild = db.query(UserGuild).filter(UserGuild.user_id == user_id, UserGuild.guild_id == guild_id).first()
    if not userguild:
        return {"message": "Member is not part of the guild"}
    else:
        raise HTTPException(status_code=403, detail="User is already an existing member of the guild")
