import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

#Allowing All Intents of Discord.
intents = discord.Intents.all()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix = '++', intents = intents)
bot.remove_command('help')

#Prints a line on console after login as a bot.
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

async def on_command_error(ctx, error):
    print(f'Error: {error}')

#Loading/Unloading Commands from cogs folder.
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'{filename} loaded')

async def main():
    await load()
    await bot.start(os.getenv('token'))
asyncio.run(main())