import logging
from os import getenv

en = getenv("ENABLE_STATS", False)
if not en or en.lower() in ["0", "false", "no"]:
    enabled = False
else:
    enabled = True

log_name = "my_id_bot"
log_level = 21  # One level higher than INFO
logger = logging.getLogger(log_name)


def setup_log():
    logging.addLevelName(log_level, log_name)
    stats = logging.getLogger(log_name)
    fh = logging.FileHandler(f"{log_name}.log")
    formatter = logging.Formatter('0.0.0.0 %(asctime)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")
    fh.setFormatter(formatter)
    stats.addHandler(fh)


def track(message):
    if enabled:
        logger.log(log_level, message)
