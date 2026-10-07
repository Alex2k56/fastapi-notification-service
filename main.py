import logging
from fastapi import FastAPI, BackgroundTasks, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from schemas import NotificationPayload, NotificationResponse
from services.notification_service import NotificationService

# Setup Structured Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    docs_url="/docs",  # Automatic Swagger UI generation
    redoc_url="/redoc"
)

# Enable Cross-Origin Resource Sharing (CORS) for production readiness
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", status_code=status.HTTP_200_OK, tags=["System Health"])
async def health_check():
    """
    Health check endpoint for container orchestrators (Docker, Kubernetes).
    """
    return {
        "status": "online",
        "app_name": settings.APP_NAME,
        "environment": "debug" if settings.DEBUG else "production"
    }


@app.post(
    f"{settings.API_V1_PREFIX}/notifications/send",
    response_model=NotificationResponse,
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Notifications"]
)
async def dispatch_notification(
        payload: NotificationPayload,
        background_tasks: BackgroundTasks
):
    """
    ASYNC DISPATCH ENDPOINT
    -----------------------
    Accepts notification requests, validates payload asynchronously,
    and delegates task execution to background workers for immediate HTTP 202 response.
    """
    try:
        response = NotificationResponse(
            status="queued",
            recipient_email=payload.recipient_email
        )

        # Offload delivery processing to background thread/coroutine
        background_tasks.add_task(
            NotificationService.process_notification,
            response.task_id,
            payload
        )

        return response

    except Exception as exc:
        logging.error(f"Failed to queue notification: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal worker queue error."
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)