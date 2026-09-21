import discord 
from discord.ext import commands

class GitHubCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

@commands.cog.listener()
async def git(self, ctx):
    await ctx.send("GitHub feature aktif!")