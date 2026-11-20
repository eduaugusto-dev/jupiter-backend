from pydantic import BaseModel
from typing import Any, Optional



class AgentContext(BaseModel):

    user_id: int

    user_name: str

    role: str

    intent: str

    action: str

    data: Optional[Any] = None

    knowledge: Optional[str] = None