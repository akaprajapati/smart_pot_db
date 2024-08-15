from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    database_url: str = "postgresql://smart_pot_user:gia@127.0.0.1:5432/smart_pot_db"
    secret_key: str = "your_secret_key"

    class Config:
        env_file = ".env"

settings = Settings()


