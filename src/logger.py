# importing libraries
import os
import sys
import logging
from datetime import datetime

# defining log file format
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# defining log file path
LOG_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)

# creating the log path folder
os.makedirs(LOG_PATH, exist_ok=True)

# joining log file with log path
LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

# defining the logging basic_config setting
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
