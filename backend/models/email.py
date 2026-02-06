from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Email(BaseModel):
    subject: str
    body: str
    category: Optional[str] = None
    confidence: Optional[float] = None
    reply: Optional[str] = None
    created_at: datetime = datetime.utcnow()
