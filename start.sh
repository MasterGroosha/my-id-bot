#!/bin/bash

# cd to script directory
cd "$(dirname "$0")" || exit 1

LOGS_DIR="/app/logs"

# If log files don't exist, create them
LOG_NORMAL="$LOGS_DIR/my_id_bot.log"
if [ ! -f "$LOG_NORMAL" ]; then
  touch "$LOG_NORMAL"
fi

LOG_ERRORS="$LOGS_DIR/err.log"
if [ ! -f "$LOG_ERRORS" ]; then
  touch "$LOG_ERRORS"
fi

# start bot
python bot.py
