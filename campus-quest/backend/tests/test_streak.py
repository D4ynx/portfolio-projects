from db.database import SessionLocal
from models.streak import StreakHistory
from services.streak_services import update_streak
from datetime import date, timedelta

test_db = SessionLocal()

test_db.query(StreakHistory).filter(StreakHistory.user_id == 3).delete()
test_db.commit()

test_streak = StreakHistory(
    user_id = 3,
    streak_count = 1,
    streak_date = date.today() - timedelta(days = 5),
    status = "active",
    streak_restore = 0
) 

test_db.add(test_streak)
test_db.commit()
test_db.refresh(test_streak)

streak_info = update_streak(3, test_db)
print(streak_info.streak_id, streak_info.streak_count, streak_info.streak_date, streak_info.status, streak_info.streak_restore)