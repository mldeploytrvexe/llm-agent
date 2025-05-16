from pydantic_settings import BaseSettings, SettingsConfigDict
import logging
import os 

class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env")
    
    HOST: str = "0.0.0.0"
    PORT: int = "8000"
    DEV_MODE: bool = True
    TITLE: str = "NTO SEARCH SERVICE"

    # Logging settings
    LOG_FORMAT: str = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    LOG_FOLDER: str = os.path.join("logs")
    LOG_FILE: str = "logs.log"
    LOG_LEVEL: int = logging.INFO


settings = Settings()