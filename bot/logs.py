import logging
from json import dumps

import structlog
from structlog import WriteLoggerFactory

from bot.config_reader import LoggingSettings, LoggingRenderer


def get_structlog_config(config: LoggingSettings) -> dict:
    return {
        "processors": get_processors(config),
        "cache_logger_on_first_use": True,
        "wrapper_class": structlog.make_filtering_bound_logger(logging.getLevelName(config.level)),
        "logger_factory": WriteLoggerFactory()
    }


def get_processors(config: LoggingSettings) -> list:
    def custom_json_serializer(data, *args, **kwargs):
        result = dict()
        # Set keys in specific order
        for key in ("timestamp", "level", "event"):
            if key in data:
                result[key] = data.pop(key)

        # Add all other fields
        result.update(**data)
        return dumps(result, default=str)

    processors = [
        structlog.processors.TimeStamper(fmt=config.format, utc=config.is_utc),
        structlog.processors.add_log_level
    ]

    if config.renderer == LoggingRenderer.JSON:
        processors.append(structlog.processors.JSONRenderer(serializer=custom_json_serializer))
    else:
        processors.append(structlog.dev.ConsoleRenderer())
    return processors
