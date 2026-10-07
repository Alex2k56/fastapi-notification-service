import asyncio
import logging
from schemas import NotificationPayload, PriorityEnum

logger = logging.getLogger("NotificationService")

class NotificationService:
    @staticmethod
    async def process_notification(task_id: str, payload: NotificationPayload) -> None:
        logger.info(f"[Task:{task_id}] Queued notification for {payload.recipient_email} with priority '{payload.priority.value}'.")
        processing_delay = 0.5 if payload.priority == PriorityEnum.HIGH else 1.5
        await asyncio.sleep(processing_delay)
        logger.info(f"[Task:{task_id}] Successfully dispatched notification to {payload.recipient_email}.")