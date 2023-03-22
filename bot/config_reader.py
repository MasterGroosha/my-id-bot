from enum import Enum

from pydantic import BaseSettings, SecretStr


class ModeEnum(str, Enum):
    DEVELOPMENT = "dev"
    PRODUCTION = "prod"


class Settings(BaseSettings):
    bot_token: SecretStr
    mode: ModeEnum = ModeEnum.PRODUCTION

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
