from models.quest import Quest
from fastapi import HTTPException
from sqlalchemy.orm import Session

def verify_quest(quest_id: int, user_id: int, db: Session):
    quest = db.query(Quest).filter(Quest.quest_id == quest_id).first()
    if not quest:
        raise HTTPException(status_code=404, detail="Record does not exist")
    if quest.user_id != user_id:
        raise HTTPException(status_code=403, detail="Unauthorized Access")
    else:
        return quest