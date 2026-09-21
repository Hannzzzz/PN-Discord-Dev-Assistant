import os
from importlib import import_module

try:
    inport_module("dotenv").load_dotenv()
except ImportError:

	pass

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
DISCORD_GUILD_ID = int(os.getenv("DISCORD_GUILD_ID", 0))

DATABASE_PATH = os.getenv("DATABASE_PATH", "database.db")
