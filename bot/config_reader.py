from enum import StrEnum, auto

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggingRenderer(StrEnum):
    JSON = auto()
    CONSOLE = auto()


class LoggingSettings(BaseSettings):
    level: str = "INFO"
    format: str = "%Y-%m-%d %H:%M:%S"
    is_utc: bool = False
    renderer: LoggingRenderer = LoggingRenderer.JSON
    log_unhandled: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="UTF-8",
        env_prefix="LOGGING_",
        extra="allow",
    )


class BotSettings(BaseSettings):
    bot_token: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="UTF-8",
        extra="allow",
    )


bot_config = BotSettings()
log_config = LoggingSettings()
