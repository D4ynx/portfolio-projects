from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from models.quest import Quest
from schemas import QuestRequest, QuestResponse, QuestStatusUpdate
from api.dependencies import get_current_user
from sqlalchemy.orm import Session

router = APIRouter()

## ENDPOINTS
@router.get("/", response_model = list[QuestResponse])
def show_quests(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
        user_quests = db.query(Quest).filter(Quest.user_id == user_id).all()
        return user_quests
        
@router.post("/", response_model = QuestResponse)
def create_quests(data: QuestRequest, user_id: int = Depends(get_current_user),  db: Session = Depends(get_db)):
        new_quest = Quest(
            quest_name = data.quest_name,
            quest_description = data.quest_description,
            xp_earned = data.xp_earned,
            quest_deadline = data.quest_deadline,
            user_id = user_id,
        )
        db.add(new_quest)
        db.commit()
        db.refresh(new_quest)
        
        return new_quest

@router.get("/{quest_id}", response_model = QuestResponse)
def show_specific_quest(quest_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
        quest = db.query(Quest).filter(Quest.quest_id == quest_id).first()
        if not quest:
            raise HTTPException(status_code=404, detail="Record does not exist")
        if quest.user_id != user_id:
            raise HTTPException(status_code=403, detail="Unauthorized access")
        else:
            return quest
        
@router.put("/{quest_id}", response_model = QuestResponse)
def update_specific_quest(quest_id: int, data: QuestRequest, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
        quest = db.query(Quest).filter(Quest.quest_id == quest_id).first()
        if not quest:
            raise HTTPException(status_code=404, detail="Record does not exist")
        if quest.user_id != user_id:
            raise HTTPException(status_code=403, detail="Unauthorized Access")
        else:
            quest.quest_name = data.quest_name
            quest.quest_description = data.quest_description
            quest.xp_earned = data.xp_earned
            quest.quest_deadline = data.quest_deadline

            db.commit()
            db.refresh(quest)
    
        return quest
    
@router.delete("/{quest_id}")
def delete_specific_quest(quest_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    
       quest = db.query(Quest).filter(Quest.quest_id == quest_id).first()
       if not quest:
           raise HTTPException(status_code=404, detail="Record does not exist")
       if quest.user_id != user_id:
            raise HTTPException(status_code=403, detail="Unauthorized Access")
       else:
            db.delete(quest)
            db.commit()
            
       return{
            "message": "Quest deleted successfully",
        }
       
@router.patch("/{quest_id}/status", response_model = QuestResponse)
def update_quest_status(data: QuestStatusUpdate, quest_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    
    quest = db.query(Quest).filter(Quest.quest_id == quest_id).first()
    if not quest:
        raise HTTPException(status_code=404, detail="Record does not exist")
    if quest.user_id != user_id:
        raise HTTPException(status_code=403, detail="Unauthorized Access")
    else:
        quest.quest_status = data.quest_status.value
        
        db.commit()
        db.refresh(quest)
    
    return quest
