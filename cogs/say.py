import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

#Making a class with command name.
class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Writing my command function using this commands.command decorator from discord.py
    @commands.command()
    @has_permissions(manage_messages=True) #Command will only work if the invoker has those permissions.
    async def say(self, ctx, *, text=''):
        await ctx.message.delete()
        if text == '':
            await ctx.send('Are you want me to say a blank message! LOL', delete_after=5)
        else:
            await ctx.send(text)

    @say.error
    async def say_error(self, error, ctx):
        if isinstance(error, CheckFailure):
            await ctx.send("It didn't worked! Wait, Do you have `manage_messages` perms?")

#Adding my class as a cog to be loaded in main.py.
async def setup(bot):
    await bot.add_cog(Say(bot))