
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class Observation(BaseModel):
    customer_query: str
    conversation_history: List[dict]
    ticket_status: Literal["open","pending","escalated","closed"]
    sentiment: Literal["negative","neutral","positive"]
    progress: float = Field(ge=0.0, le=1.0)

class Action(BaseModel):
    action_type: Literal["classify","respond","resolve","escalate"]
    category: Optional[Literal["account","billing","security","other"]] = None
    response_text: Optional[str] = None

class Reward(BaseModel):
    score: float
    feedback: str
