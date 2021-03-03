import logging
import os
import sys
import time
from logging import basicConfig
from logging import DEBUG
from logging import getLogger
from logging import INFO

from telethon import TelegramClient
from telethon.sessions import StringSession

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)
ENV = bool(os.environ.get("ENV", True))

StartTime = time.time()
CMD_LIST = {}
CMD_HELP = {}
LOAD_PLUG = {}
LUNA_VERSION = "1.1.2"

if ENV:
    TOKEN = os.environ.get("TOKEN", None)
    API_KEY = os.environ.get("API_KEY", None)
    API_HASH = os.environ.get("API_HASH", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    tbot = TelegramClient(None, API_KEY, API_HASH)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
    CONSOLE_LOGGER_VERBOSE = os.environ.get("CONSOLE_LOGGER_VERBOSE", "False")
    BOT_ID = int(os.environ.get("BOT_ID", None))
    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=DEBUG
        )
    else:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
        )
    LOGS = getLogger(__name__)

    if STRING_SESSION:
        ubot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
    else:
        sys.exit(1)

    try:
        ubot.start()
    except BaseException:
        print("String Session Not working!")
        sys.exit(1)

else:
    sys.exit(1)
