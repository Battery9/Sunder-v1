import discord
from discord.ext import commands
import configparser

#Reading data file with ConfigParser. Used specific keys for each commands.
config = configparser.ConfigParser()
config.read('res/data.ini')

#Making a class with command name.
class Set(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Writing my command function using this commands.command decorator from discord.py
    @commands.group()
    async def set(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Usage:\n`popular`:To set popular section on Tournament embed. Pass empty arg to hide.")

    @set.command()
    async def popular(self, ctx, *, text=''):
        ##To Modify popular key of data.ini
        config['var']['popular'] = text
        with open('res/data.ini', 'w') as f:
            config.write(f)
        await ctx.send('Edited. Check help command.', delete_after=5)

    @set.command()
    async def status(self, ctx, *, text='online'):
        config['var']['status'] = text
        with open('res/data.ini', 'w') as f:
            config.write(f)
        await ctx.send("Done. Reboot the bot to display changes.")

    @set.command()
    async def activity(self, ctx, *, text='playing,something wrong'):
        config['var']['activity'] = text
        with open('res/data.ini', 'w') as f:
            config.write(f)
        await ctx.send("Done. Reboot the bot to display changes.")


#Adding my class as a cog to be loaded in main.py.
async def setup(bot):
    await bot.add_cog(Set(bot))