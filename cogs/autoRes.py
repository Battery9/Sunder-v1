from discord import Embed, ButtonStyle, Interaction
from discord.ui import View, button, Button
from discord.ext import commands
import configparser
import random

#getting saved triggers and responses from ini file and making a list
config = configparser.ConfigParser()
config.read('res/responses.ini')
##help res
help_triggers = config['help']['trigger'].split(',')
help_res = config['help']['response'].split('|')
##scrims res
scrims_triggers = config['scrims']['trigger'].split(',')
scrims_res = config['scrims']['response'].split('|')



#Making a class with eventListener name.
class AutoRes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        ##Default Buttons and interaction functions to be added with embed
        class view(View):
            @button(label="Yes!", style=ButtonStyle.green)
            async def yes(self, interaction: Interaction, button:Button):
                await interaction.message.delete()
                await ctx.invoke(help_command)
            @button(label="No thanks.", style=ButtonStyle.red)
            async def no(self, interaction: Interaction, button:Button):
                await interaction.message.delete()
        class view2(View):
            @button(label="Yes!", style=ButtonStyle.green)
            async def yes(self, interaction: Interaction, button:Button):
                await interaction.message.delete()
                embed = Embed(title="**__❑ On-going Tournaments and Scrims__**", description="**>> Please visit the below channel to learn about and join different events happening right now across different platforms of UREsports. Our only talented admin have listed all the Scrims and Tournament just for you. Unleash your talents, show off your skills and roast your opponents with your squad.\nIt’s time to have some fun and make some noise**\n\n<#1125346374737727530>", color=0x00ff00).set_footer(text="Sunder | UREsports")

                ##Reading the ini file inside res to use.
                config.read('res/data.ini')
                popular = config['var']['popular']
                if(popular!=''):
                    embed.add_field(name="__❑ Popular: __", value=popular)
                await interaction.response.send_message(embed=embed, delete_after=50)
            @button(label="No thanks.", style=ButtonStyle.red)
            async def no(self, interaction: Interaction, button:Button):
                await interaction.message.delete()

        ##Looking for matching words in messages and giving reply(help)
        for triger in help_triggers:
            if triger in message.content.lower() and not message.content.startswith(('+', '/', '!', '#', '@', '-', '.', '?')): #Add more elements into the startwith tuple to be ignored by the bot.
                ctx = await self.bot.get_context(message)
                help_command = self.bot.get_command('help')
                embed = Embed(title=random.choice(help_res), color=0x00ff00)
                embed.set_thumbnail(url="https://i.ibb.co/LC96Nb1/ezgif-com-gif-maker.gif")
                await message.channel.send(embed=embed, view=view(), delete_after=15)

        for trigger in scrims_triggers:
             if trigger in message.content.lower():
                embed = Embed(title=random.choice(scrims_res), color=0x00ff00)
                embed.set_thumbnail(url="https://i.ibb.co/LC96Nb1/ezgif-com-gif-maker.gif")
                await message.channel.send(embed=embed, view=view2(), delete_after=15)
    

#Adding my class as a cog to be loaded in main.py.
async def setup(bot):
    await bot.add_cog(AutoRes(bot))