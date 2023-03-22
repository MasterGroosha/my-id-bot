import logging

import structlog
from structlog import PrintLoggerFactory

from config_reader import ModeEnum


def get_structlog_config(mode: ModeEnum) -> dict:
    log_level = logging.DEBUG if mode == ModeEnum.DEVELOPMENT else logging.WARNING
    return {
        "processors": get_processors(mode),
        "cache_logger_on_first_use": True,
        "wrapper_class": structlog.make_filtering_bound_logger(log_level),
        "logger_factory": PrintLoggerFactory()
    }


def get_processors(mode: ModeEnum) -> list:
    if mode == ModeEnum.DEVELOPMENT:
        datetime_format = "%Y-%m-%d %H:%M:%S"
    else:
        datetime_format = "%Y-%m-%d %H:%M UTC"

    shared_processors = [
        structlog.processors.TimeStamper(fmt=datetime_format, utc=mode == ModeEnum.PRODUCTION, key="timestamp"),
        structlog.processors.add_log_level
    ]

    options = {
        ModeEnum.DEVELOPMENT: shared_processors + [  # noqa
            structlog.processors.KeyValueRenderer()
        ],
        ModeEnum.PRODUCTION: shared_processors + [
            structlog.processors.dict_tracebacks,
            structlog.processors.JSONRenderer(),
        ]
    }
    return options[mode]
