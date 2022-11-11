# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")



BOT_TOKEN = os.getenv("BOT_TOKEN")



__all__ = ["Config"]

import os

from dotenv import load_dotenv

if os.path.isfile("config.env"):
    load_dotenv("config.env")


class Config:
    """ assistant configs """
    APP_ID = int(os.environ.get("APP_ID", 0))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/cbe826936d4de9ec1838a.jpg")
    BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
    if not BLACKLIST_CHAT:
        BLACKLIST_CHAT = [-1001473548283]
    BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
    BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
    BOT_VER = "0.1.0@main"
    BRANCH = "main"
    CHANNEL = getenv("CHANNEL", "ruangprojects")
    CMD_HANDLER = getenv("CMD_HANDLER", ".")
    DB_URL = getenv("DATABASE_URL", "")
    GROUP = getenv("GROUP", "ruangdiskusikami")
    HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
    STRING_SESSION = getenv("STRING_SESSION", "")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
    AUTH_CHATS = set([-1001638078842])  #
    if os.environ.get("AUTH_CHATS"):
        AUTH_CHATS.update(map(int, os.environ.get("AUTH_CHATS").split()))
    WHITELIST_CHATS = set([-1001638078842])  # 
    if os.environ.get("WHITELIST_CHATS"):
        WHITELIST_CHATS.update(map(int, os.environ.get("WHITELIST_CHATS").split()))
    DEV_USERS = (
        1441342342,  # fkm
        5089916692,  # @Punya_alby
    )
    ADMINS = {}
