from pydantic import BaseModel, ConfigDict
from enum import Enum
from datetime import date

class GuildStatus(Enum):
    active = "active"
    inactive = "inactive"
    
class GuildRole(Enum):
    guild_master = "guild_master"
    officer = "officer"
    member = "member"
    
class GuildRequest(BaseModel):
    guild_name : str
    guild_description : str

class GuildResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    guild_id : int
    guild_name : str
    guild_description : str
    status : GuildStatus
    created_by : int
    created_at : date 
    
class GuildMemberResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    user_guild_id : int
    guild_id : int
    user_id : int
    joined_at : date
    role : GuildRole
    xp_contributed : int
    last_activity : date