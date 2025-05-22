from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Wikipedia Content Analyzer"
    API_V1_STR: str = "/api/v1"

    # Database settings
    DATABASE_URL: str

    # Wikipedia API settings (opcional, si se necesita alguna config específica)
    WIKIPEDIA_USER_AGENT: str = "MyWikipediaApp/1.0 (myemail@example.com)" # Cambiar email

    class Config:
        case_sensitive = True
        env_file = [".env", "backend/.env"]
        env_file_encoding = "utf-8"

settings = Settings()
