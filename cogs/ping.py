import discord
from discord.ext import commands

#Making a class with command name.
class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Writing my command function using this commands.command decorator from discord.py
    @commands.command()
    async def ping(self, ctx):
        latency = self.bot.latency * 1000
        await ctx.send(f'Pong! Latency is {latency:.2f} ms')

#Adding my class as a cog to be loaded in main.py.
async def setup(bot):
    await bot.add_cog(Ping(bot))