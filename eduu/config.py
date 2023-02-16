import os.path

from typing import List, Optional


API_ID: int = 21757852
API_HASH: str = "90016a3532ceebc1d6f9b3da5917b37c"
TOKEN: str = "6131140627:AAGOJMYaT7Ce4Mop6d1zUbuCqjRJsGfyjHg"

log_chat: int = -1001801784157
sudoers: List[int] = [1265929515, 1265929515]
super_sudoers: List[int] = [1265929515, 1265929515]

prefix: List[str] = ["/", "!", ".", "$", "-"]

disabled_plugins: List[str] = []

WORKERS = 24

DATABASE_PATH = os.path.join("eduu", "database", "eduu.db")

TENOR_API_KEY: Optional[str] = "X9HD35B7ZGP6"

sudoers.extend(super_sudoers)

# notes

# 1. api_id & api_hash get from my.telegram.org
# 2. token fill with your bot_token get from @BotFather
# 3. log_chat fill with the chat id of a group that you should create for the bot logger
# 4. [optional] var disabled_plugins let you to disable an plugin to be loaded. Example:
# You don't want the youtube plugin to be loaded, then fill disabled_plugins var with youtube (or any name of the plugins file)
