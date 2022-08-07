# <--IMPORTS-->
import os
from telethon import TelegramClient
from telethon.session import StringSession

# <-- Taking Configration -->
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
TOKEN = os.environ.get("TOKEN", "")
SESSION = os.environ.get("SESSION", "")


if TOKEN: # <-- if Bot Token Given -->
    bot = TelegramClient("dynamic", API_ID, API_HASH).start(bot_token=TOKEN)
    print("FOund BOT_ToKEN Activating Bot client!")
    print("\n\n")
    print(".......")
    bot.run_until_disconnected()
elif SESSION: # <-- if Session Given -->
    session = str(SESSION)
    app = TelegramClient(StringSession(session), API_ID, API_HASH)
    print("Found STring Session Activating user Clint")
    print("\n\n")
    print(".......")
    app.run_until_disconnected()
else: # <-- if not then you are Stupid -->
    print("Stupid Enter Bot Token or String session!")