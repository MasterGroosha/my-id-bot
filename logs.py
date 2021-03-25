import logging
from os import getenv, path, mkdir

en = getenv("ENABLE_STATS", False)
if not en or en.lower() in ["0", "false", "no"]:
    enabled = False
else:
    enabled = True

if not path.exists("logs"):
    mkdir("logs")


stats_log_name = "my_id_bot"
stats_log_level = 21  # One level higher than INFO
stats_logger = logging.getLogger(stats_log_name)

errors_log_name = "errors"
errors_logger = logging.getLogger(errors_log_name)


def setup_stats_log():
    logging.addLevelName(stats_log_level, stats_log_name)
    fh = logging.FileHandler(f"logs/{stats_log_name}.log")
    formatter = logging.Formatter('%(asctime)s - %(message)s', "%Y-%m-%d %H:%M:%S")
    fh.setFormatter(formatter)
    stats_logger.addHandler(fh)


def setup_errors_log():
    error_fh = logging.FileHandler(f"logs/err.log")
    error_fh.setFormatter(logging.Formatter('%(asctime)s - %(message)s', "%Y-%m-%d %H:%M:%S"))
    errors_logger.addHandler(error_fh)


def track(message):
    if enabled:
        stats_logger.log(stats_log_level, message)
