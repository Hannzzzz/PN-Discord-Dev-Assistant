import os
from importlib import import_module

try:
	import_module("dotenv").load_dotenv()
except ImportError:
	# dotenv is optional; environment variables can still be provided normally.
	pass


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
DISCORD_GUILD_ID = int(os.getenv("DISCORD_GUILD_ID", 0))

DATABASE_PATH = os.getenv("DATABASE_PATH", "developer_bot.db")
