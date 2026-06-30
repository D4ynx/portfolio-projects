from models.streak import StreakHistory
from sqlalchemy.orm import Session
from services.auth_services import get_user_by_id
from datetime import date

#create streak
def create_streak(user_id: int, db: Session):
    user = get_user_by_id (user_id, db)
    
    new_streak_record = StreakHistory(
        user_id = user.user_id,
        streak_count = 1,
        streak_date = date.today(),
        status = "active",
        streak_restore = 5,
    )
    
    db.add(new_streak_record)
    db.commit()
    db.refresh(new_streak_record)
    
    return new_streak_record
    
#increase streak
def increase_streak(user_id: int, db: Session):
    user = get_user_by_id(user_id, db)
    latest_streak_record = db.query(StreakHistory).filter(StreakHistory.user_id == user.user_id).order_by(StreakHistory.streak_date.desc()).first()
    
    new_streak_record = StreakHistory(
        user_id = user.user_id,
        streak_count = latest_streak_record.streak_count + 1,
        streak_date = date.today(),
        status = "active",
        streak_restore = latest_streak_record.streak_restore,
    )
    
    db.add(new_streak_record)
    db.commit()
    db.refresh(new_streak_record)

    return new_streak_record

#restore streak
def restore_streak(user_id:int, db: Session):
    user = get_user_by_id(user_id, db)
    latest_streak_record = db.query(StreakHistory).filter(StreakHistory.user_id == user.user_id).order_by(StreakHistory.streak_date.desc()).first()
    
    new_streak_record = StreakHistory(
        user_id = user.user_id,
        streak_count = latest_streak_record.streak_count,
        streak_date = date.today(),
        status = "retained",
        streak_restore = latest_streak_record.streak_restore - 1,
    )
    
    db.add(new_streak_record)
    db.commit()
    db.refresh(new_streak_record)
    
    return new_streak_record


#break streak
def break_streak(user_id: int, db:Session):
    user = get_user_by_id(user_id, db)
    latest_streak_record = db.query(StreakHistory).filter(StreakHistory.user_id == user.user_id).order_by(StreakHistory.streak_date.desc()).first()
    
    new_streak_record = StreakHistory(
        user_id = latest_streak_record.user_id,
        streak_count = 0,
        streak_date = date.today(),
        status = "broken",
        streak_restore = latest_streak_record.streak_restore,
    )
    
    db.add(new_streak_record)
    db.commit()
    db.refresh(new_streak_record)
    
    return new_streak_record

def update_streak(user_id: int, db: Session):
    #fetch latest record //
    #calculate day gap //
    #call the right function //
    
    user = get_user_by_id (user_id, db)
    latest_streak_record = db.query(StreakHistory).filter(StreakHistory.user_id == user.user_id).order_by(StreakHistory.streak_date.desc()).first()

    if latest_streak_record is None:
        return create_streak(user.user_id, db)
    
    else:
        gap = date.today() - latest_streak_record.streak_date
        
        if gap.days == 0:
            return latest_streak_record
        
        elif gap.days == 1:
            return increase_streak(user.user_id, db)
            
        elif gap.days >= 2:
            if latest_streak_record.streak_restore > 0:
                return restore_streak(latest_streak_record.user_id, db)
        
            else:
                return break_streak(latest_streak_record.user_id, db)
        