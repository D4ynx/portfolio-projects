from pydantic import BaseModel, ConfigDict
from enum import Enum
from datetime import date

class QuestStatus(Enum):
    completed = "completed"
    incomplete = "incomplete"
    not_started = "not_started"

## Pydantic Models - Request
class QuestRequest(BaseModel):
    quest_name : str
    quest_description: str
    xp_earned : int
    quest_deadline : date
    
## Pydantic Models - Response
class QuestResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    quest_id : int
    quest_name : str
    quest_description: str
    xp_earned : int
    quest_deadline: date
    quest_status: QuestStatus