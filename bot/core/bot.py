import discord
from discord.ext import commands
from core.plugin_manager import load_plugins

intents = discord.intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"Bot login sebagai {bot.user}")

    await load_plugins(bot)



