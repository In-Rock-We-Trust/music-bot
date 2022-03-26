import discord
from discord.ext import commands
from discord.ext.commands.bot import when_mentioned_or
import os
import coloredlogs
import logging
from pathlib import Path
from dotenv import load_dotenv
cwd = Path(__file__).parents[0]
cwd = str(cwd)
load_dotenv()


log = logging.getLogger("Bot")
coloredlogs.install(logger=log)
logging.basicConfig(level=logging.INFO, format="(%(asctime)s) %(levelname)s %(message)s",
                    datefmt="%m/%d/%y - %H:%M:%S %Z")  
log.propagate = False

if not os.getenv("BOT_TOKEN"):
    log.error("You forgot the token")
    exit(1)

bot = commands.Bot(command_prefix=when_mentioned_or("$"), intents=discord.Intents.all())

if __name__ == '__main__':
    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")


bot.run(os.getenv("BOT_TOKEN"))