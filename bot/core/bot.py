import os
from http import client

from os import discord
from discord import commands
from core.plugin_manager import load_plugins

intents = discord.intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(intents=intents, help_command=None)


@client.event
async def on_ready():
    print(f"Bot berhasil login sebagai {client.user}")

    await load_plugins(client)

client.run(client.getenv("DISCORD_TOKEN"))



