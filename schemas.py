from pydantic import BaseModel, EmailStr, Field
from enum import Enum
from datetime import datetime
from typing import Optional
import uuid

class PriorityEnum(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class NotificationPayload(BaseModel):
    """
    DATA TRANSFER OBJECT (DTO)
    --------------------------
    Strict validation schema for incoming HTTP notification requests.
    Automatic payload validation prevents invalid data from entering the service layer.
    """
    recipient_email: EmailStr = Field(..., description="Target email address")
    subject: str = Field(..., min_length=3, max_length=100, example="System Alert")
    message: str = Field(..., min_length=5, max_length=1000)
    priority: PriorityEnum = PriorityEnum.MEDIUM

class NotificationResponse(BaseModel):
    """
    RESPONSE DTO
    ------------
    Standardized JSON API output contract.
    """
    task_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    status: str
    recipient_email: EmailStr
    queued_at: datetime = Field(default_factory=datetime.utcnow)