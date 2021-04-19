# Imports
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import datetime

# Bot Prefix
# Feel free to update this to take a file input or something
# So that the prefix can be changed in discord by admin
BOT_PREFIX = "."

# Tokens to be used for bot within .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

Client = discord.Client()
bot = commands.Bot(command_prefix=BOT_PREFIX)

# Add yer cogs here pal
extensions = []


# Some information to display in terminal to display bot status
@bot.event
async def on_ready():
    time = datetime.datetime.now().strftime('%d/%b/%y')
    print(f'Powering up...\nActivated on {time}')
    await bot.change_presence(activity=discord.Game('Command Prefix: .'))
    if __name__ == '__main__':
        for ext in extensions:
            bot.load_extension(ext)


# Error Handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass all required arguments')


bot.run(TOKEN)
