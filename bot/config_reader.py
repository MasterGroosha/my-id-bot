from enum import Enum

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


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
    log_unhandled: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="LOGGING_",
        extra="allow",
    )


class BotSettings(BaseSettings):
    bot_token: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )


bot_config = BotSettings()
log_config = LoggingSettings()
