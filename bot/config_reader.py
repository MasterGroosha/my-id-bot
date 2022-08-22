from pydantic import BaseSettings


class Settings(BaseSettings):
    bot_token: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
