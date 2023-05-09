from enum import Enum

from pydantic import BaseSettings, SecretStr


class ModeEnum(str, Enum):
    DEVELOPMENT = "dev"
    PRODUCTION = "prod"


class LoggingRenderer(str, Enum):
    JSON = "json"
    CONSOLE = "console"


class LoggingSettings(BaseSettings):
    level: str = "INFO"
    format: str = "%Y-%m-%d %H:%M:%S"
    is_utc: bool = False
    renderer: LoggingRenderer = LoggingRenderer.JSON

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = "LOGGING_"


class BotSettings(BaseSettings):
    bot_token: SecretStr

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


bot_config = BotSettings()
log_config = LoggingSettings()
