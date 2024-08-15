from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str = "your_secret_key"

    class Config:
        env_file = ".env"  # Optional: Loads variables from a .env file for local development

settings = Settings()

# Optional: Log to ensure the correct database URL is being used
print(f"Connecting to database at: {settings.database_url}")
