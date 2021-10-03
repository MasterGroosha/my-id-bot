from dataclasses import dataclass
from os import getenv


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    bot: TgBot


def load_config():
    return Config(
        bot=TgBot(
            token=getenv("BOT_TOKEN"),
        )
    )
