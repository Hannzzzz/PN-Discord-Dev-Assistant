import io
import discord	
from discord.ext import commands
from pylint.reporters.text import TextReporter
from pylint.lint import Run


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents) # temporary prefix


@bot.command(name = 'analyze')
async def analyze_code(ctx, *, code: str = None):
    """Analyze the provided code using Pylint and return the results."""

	if not code:
		await ctx.send("Please provide the code to analyze.")
		return

	if code.startswith('```python'):
		code = code[10:-3]  

	elif code.startswith('```'):
		code = code[3:-3]:

	