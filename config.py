import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    APPLICATION SETTINGS MANAGEMENT
    -------------------------------
    Parses environment variables with fallback defaults.
    Ensures safe configuration across Development, Staging, and Production.
    """
    APP_NAME: str = "Enterprise Notification Dispatcher"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1")
    API_V1_PREFIX: str = "/api/v1"
    MAX_CONCURRENT_WORKERS: int = 10

    # Rate Limiting Configuration
    RATE_LIMIT_PER_MINUTE: int = 60


settings = Settings()