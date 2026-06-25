from schemas import GuildResponse, GuildRequest, GuildMemberResponse
from fastapi import Depends, HTTPException, APIRouter
from models.guild import Guild
from models.user_guilds import UserGuild
from db.database import get_db
from services.guild_services import verify_membership, verify_guild, verify_owner
from services.auth_services import get_current_user
from sqlalchemy.orm import Session

router = APIRouter()

##POST ENDPOINT
@router.post("/", response_model=GuildResponse)
def create_guild(data: GuildRequest, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
        new_guild = Guild(
            guild_name = data.guild_name,
            guild_description = data.guild_description,
            created_by = user_id,
        )
        
        db.add (new_guild)
        db.commit()
        db.refresh(new_guild)
        
        guild_leader = UserGuild(
            guild_id = new_guild.guild_id,
            user_id = user_id,
            role = "guild_master"
        )
        
        db.add(guild_leader)
        db.commit()
        db.refresh(guild_leader)
        
        return new_guild

##List of all guilds
@router.get("/", response_model= list[GuildResponse])
def show_guilds(db: Session = Depends(get_db)):
    guilds = db.query(Guild).all()
    return guilds

#Get one guild
@router.get("/{guild_id}", response_model=GuildResponse)
def show_specific_guild(guild_id: int, db: Session = Depends(get_db)):
    guild = db.query(Guild).filter(Guild.guild_id == guild_id).first()
    return guild

#Join a guild
@router.post("/{guild_id}/join", response_model=GuildMemberResponse)
def join_guild(guild_id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    verify_guild(guild_id, db)
    verify_membership(guild_id, user_id, db) 

    member = UserGuild(
        guild_id = guild_id,
        user_id = user_id,
        role = "member",
    )
    
    db.add(member)
    db.commit()
    db.refresh(member)
    
    return member
    
    
#Leave a guild
@router.delete("/{guild_id}/leave")
def leave_guild(guild_id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    verify_guild(guild_id, db)
    
    user = db.query(UserGuild).filter(UserGuild.user_id == user_id, UserGuild.guild_id == guild_id).first()
    
    if user:
        db.delete(user)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="User does not belong to the guild") 
    
    return{
         "message" : "Guild left successfully",
    }
     

#Retrieve members of guild
@router.get("/{guild_id}/members", response_model = list[GuildMemberResponse])
def retrieve_members(guild_id: int, db: Session = Depends(get_db)):
    verify_guild(guild_id, db)
    
    users = db.query(UserGuild).filter(UserGuild.guild_id == guild_id).all()
    
    return users

#Delete a guild
@router.delete("/{guild_id}")
def delete_guild(guild_id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    guild = verify_guild(guild_id,db)
    verify_owner(guild_id, user_id, db)
    
    db.delete(guild)
    db.commit()
    
    return{
        "message": "Guild successfully deleted"
    }