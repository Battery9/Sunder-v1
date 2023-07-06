import discord
from discord.ext import commands
import os
import asyncio
import configparser
from dotenv import load_dotenv
load_dotenv()

#Allowing All Intents of Discord.
intents = discord.Intents.all()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix = '++', intents = intents)
bot.remove_command('help')

##Reading the data.ini file. Getting custom activity from their.
config = configparser.ConfigParser()
config.read('res/data.ini')
activity = config["var"]["activity"]
status = config['var']['status']

##Config custom activity and status as per Discord util
activity = activity.split(",")
if activity[0] == 'playing':
    activity=discord.Game(name=activity[1])
elif activity[0] == 'streaming':
    activity=discord.Streaming(name=activity[1], url=activity[2] if len(activity) > 2 else "http://cutt.ly/ure-dc")
elif activity[0] == 'listening':
    activity=discord.Activity(type=discord.ActivityType.listening, name=activity[1])
else:
    activity=discord.Activity(type=discord.ActivityType.watching, name=activity[1])

if status == "dnd":
    status = discord.Status.dnd
elif status == 'idle':
    status = discord.Status.idle
else:
    status = discord.Status.online


#Prints a line on console after login as a bot.
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    ##Set Bot Activity
    try:
        await bot.change_presence(status=status, activity=activity)
    except Exception as e:
        print(e)

##Basic Command error log
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